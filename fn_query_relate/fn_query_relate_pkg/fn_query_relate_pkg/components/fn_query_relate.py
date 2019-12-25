'''
Eliriana Lleshi
eliriana.lleshi@tufts.edu
Information Security Software Engineer
TTS Information Security
Tufts University
Summer 2019
'''

# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_query_relate"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_query_relate_pkg", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_query_relate_pkg", {})

    @function("fn_query_relate")
    def _fn_query_relate_function(self, event, *args, **kwargs):
        """Function: Completes the AutoPhish workflow by querying each artifact within the entire dataset of artifacts,
         escalating incidents if necessary, and relating incidents to each other through artifacts."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #yield StatusMessage("starting...")

    # Getting artifact data from Resilient

            # All incident IDs
            uri_inc = "/incidents"
            all_inc = self.rest_client().get(uri_inc)                         # REST API gets JSON of all incidents
            all_inc_ids = []
            for x in range(0, len(all_inc)):
                if ((all_inc[x]['properties']['case_type']) == 495):          # only known malignant ('Incident' type)
                    all_inc_ids.append(all_inc[x]['id'])

            all_values = []                                            # all_values[] will contain all artifact values
                                                                       # on an instance of Resilient
            for x in range(0, len(all_inc_ids)):
                temp_inc_id = all_inc_ids[x]
                uri_art = "/incidents/{0}/artifacts".format(temp_inc_id)
                artifacts = self.rest_client().get(uri_art)

                for x in range(0, len(artifacts)):
                    all_values.append(artifacts[x]['value'])

    # Get all artifacts of current 'Phishing' incident (incident specific data)
            uri_art = "/incidents/{0}/artifacts".format(incident_id)
            artifacts = self.rest_client().get(uri_art)        # REST API gets JSON of all its artifacts
            curr_inc_values = []                               # array of all artifact values of a single incident
            for x in range(0, len(artifacts)):
                curr_inc_values.append(artifacts[x]['value'])


    # Query each artifact in the incident (curr_inc_values) within the set of all artifacts (all_values)
            match = False
            intersection = set.intersection(set(curr_inc_values), set(all_values))
            if (len(intersection) != 0):
                match = True

            #yield StatusMessage("done...")

            results = {
                "match": match
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()