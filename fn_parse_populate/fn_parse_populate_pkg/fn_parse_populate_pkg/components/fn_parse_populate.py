'''
Eliriana Lleshi
eliriana.lleshi@tufts.edu
Tufts University
Summer 2019
'''

# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging, re, requests, json
from resilient_lib import get_file_attachment
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

import datetime
import json
import eml_parser


def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_parse_populate"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_parse_populate_pkg", {})
        self.incident_id = []
        self.attachment_id = []
        self.attachment_content = []

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_parse_populate_pkg", {})

    @function("fn_parse_populate")
    def _fn_parse_populate_function(self, event, *args, **kwargs):
        """Function: Parses an incident's .eml file attachment (forwarded email) and populates the incident with artifacts given the information within the file."""
        try:
            #yield StatusMessage("starting...")

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            incident_id = kwargs.get("incident_id")                 # Get the function parameter
            self.incident_id = incident_id

            uri_attach = "/incidents/{0}/attachments".format(incident_id)
            attachments = self.rest_client().get(uri_attach)        # REST API gets JSON of all attachments

            if (len(attachments) == 0):                             # no attachments, original artifacts maintained
                no_attach = True
                body_content = ''
                subject = ''
                recipient = ''
                sender = ''
                date = ''
                file_md5_hash = ''
                file_sha1_hash = ''
                file_sha256_hash = ''
                file_name = ''
                note_header = ''
                ips = []
                urls = []
            else:
                no_attach = False

                # Delete existing artifacts pertaining to reporting email (not the attached email)
                uri_art = "/incidents/{0}/artifacts".format(incident_id)
                artifacts = self.rest_client().get(uri_art)  # REST API gets JSON of all artifacts
                for x in range(0, len(artifacts)):  # loop though all artifacts
                    artifact_id = artifacts[x]['id']
                    uri_delete = "/incidents/{0}/artifacts/{1}".format(incident_id, artifact_id)
                    self.rest_client().delete(uri_delete)  # REST API deletes old artifact

                attachment = attachments[0]                             # could be expanded for multiple attachments
                attachment_id = attachment['id']                        # isolates attachment ID

                # Use eml-parser to handle the .eml attachment containing the suspicious email
                attachment_content = get_file_attachment(self.rest_client(), str(incident_id),
                                                         attachment_id=str(attachment_id))
                parsed_eml = eml_parser.eml_parser.decode_email_b(attachment_content,
                                                                  include_raw_body=True, include_attachment_data=True)
                sorted_eml = json.loads(json.dumps(parsed_eml, default=json_serial))


                # Isolating artifacts from parsed eml file, to be added in Post-Processing script
                header = sorted_eml['header']
                body_content = sorted_eml['body'][0]['content']
                subject = header['subject']
                recipient = str(header['to']).strip("['']")
                sender = header['from']
                date = header['date']
                note_header = str(attachment_content.decode())
                ips = list(set(re.findall(r'(?<=\[)\d{1,3}(?:\.\d{1,3}){3}(?=\])', note_header))) #unique list of IPs found in the header
                url_list = eml_parser.eml_parser.get_uri_ondata(str(parsed_eml))
                urls = list(set(url_list))  #unique list of URLs found in the header


                # Suspicious email may or may not have an attachment
                try:
                    file_name = sorted_eml['attachment'][0]['filename']
                    file_hashes = sorted_eml['attachment'][0]['hash']
                    file_md5_hash = file_hashes['md5']
                    file_sha1_hash = file_hashes['sha1']
                    file_sha256_hash = file_hashes['sha256']
                except KeyError:
                    file_md5_hash = 'NULL'
                    file_sha1_hash = 'NULL'
                    file_sha256_hash = 'NULL'
                    file_name = 'NULL'

                # Logging
                log = logging.getLogger(__name__)
                log.info("incident_id: %s", incident_id)
                log.info("attachment_id: %s", attachment_id)
                #log.info("attachment_content: %s", attachment_content)

            #yield StatusMessage("done...")

            results = {
                # Return all Artifacts here and addArtifact() in Post-Processing script
                "body": body_content,
                "subject": subject,
                "recipient": recipient,
                "sender": sender,
                "date": date,
                "file_md5_hash": file_md5_hash,
                "file_sha1_hash": file_sha1_hash,
                "file_sha256_hash": file_sha256_hash,
                "file_name": file_name,
                "header": note_header,
                "no_attach": no_attach,
                "urls": urls,
                "ips": ips
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
