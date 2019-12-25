AutoPhish is a workflow within the IBM Resilient Platform which includes two
functions, both of which are included in this repository. AutoPhish runs after 
the Generic Email Script (`email_parsing_script.py`) determines that an email concerns
phishing or scams. AutoPhish then parses email attachments, populates incident
artifacts with information, then checks the data store on Resilient to determine
whether the threats have been seen before. Incidents are escalated from events
to incidents if they are known to be malignant. Knowing this helps analysts relate 
incidents and automates the analysis process (from analyzing email headers to 
response to assigned tasks).

See "AutoPhish Documentation.pdf" for background on the Resilient platform 
and where the AutoPhish project falls into the entire architecture. A development and installation walkthrough, as well as the Pre-Process and Post-Process scripts can be found there, as well. 

The folders `fn_parse_populate` and `fn_query_relate` include the entire package 
downloaded with `--codegen`, which provides all the necessary paths to successfully 
integrate with the platform and test in development. These don't have to be touched 
during customization. A `tar.gz` of the function allows it to be integrated with any 
Resilient instance, and the entire function package allows it to be generated.

The files containing the function implementations themselves are 
`fn_parse_populate.py` and `fn_query_relate.py`, and their relative paths are 
provided below. Pre-processing and Post-processing scripts for both functions are also provided. 
I have gone ahead and packaged the functions and the `tar.gz` files can be found here as well:

PARSE AND POPULATE:
-  function code: 
`fn_parse_populate/fn_parse_populate_pkg/fn_parse_populate_pkg/components/fn_parse_populate.py`
-  tar.gz:
`fn_parse_populate/fn_parse_populate_pkg/dist/fn_parse_populate_pkg-1.0.0.tar.gz`

Pre-Processing Script:
```python
inputs.incident_id = incident.id
```
Post-Processing Script:
```python
if (results.no_attach == False):  # there is an attachment
    incident.addArtifact("Email Subject", str(results.subject), "")
    incident.addArtifact("Email Body", str(results.body),"")
    incident.addArtifact("Email Recipient", str(results.recipient), "")
    incident.addArtifact("Email Sender", str(results.sender), "")
    incident.addNote(str(results.header))

    if (results.urls != []):
        for x in range(0, len(results.urls)):
            url = str(results.urls[x])
            incident.addArtifact("URL", url, "")
            #incident.addNote(str(results.urls[x]))

    if (results.ips != []):
        for x in range(0, len(results.ips)):
            ip = str(results.ips[x])
            incident.addArtifact("IP Address", ip, "")
            #incident.addNote(str(results.ips[x))


    if (results.file_name != "NULL"):
        incident.addArtifact("File Name", str(results.file_name), "")
        incident.addArtifact("file_md5_hash", str(results.file_md5_hash), "")
        incident.addArtifact("file_sha1_hash", str(results.file_sha1_hash), "")
        incident.addArtifact("file_sha256_hash", str(results.file_sha256_hash), "")
    
# no artifacts added if no attachment exists
```

QUERY AND RELATE:
-  function code: 
`fn_query_relate/fn_query_relate_pkg/fn_query_relate_pkg/components/fn_query_relate.py` 
-  tar.gz:
`fn_query_relate/fn_query_relate_pkg/dist/fn_query_relate_pkg-1.0.0.tar.gz`

Pre-Processing Script:
```python
inputs.incident_id = incident.id
```
Post-Processing Script:
```python
# As more Phishing data appears on Resilient, it may be useful to comment out addTask() lines 
# and automate the closing of incidents by uncommenting the other lines

if (results.match == True):
    incident.properties.case_type = "Incident"
    incident.addTask("Close Incident", "Complete", 'Confirm automatic analysis was satisfactory and close incident')
    #incident.plan_status = 'C'
    #incident.resolution_id = 'Resolved'
    #incident.resolution_summary = 'Automatically closed by AutoPhish workflow -- Match Detected'
else:
    incident.addTask("Close Incident", "Complete", 'Close incident after manual review')
    incident.addTask("Manual Review", "Analysis", 'Analyze artifacts manually, phishing attack may not have been seen before')
    #incident.plan_status = 'C'
    #incident.resolution_id = 'Unresolved'
    #incident.resolution_summary = 'Automatically closed by AutoPhish workflow -- No Match Detected'
```

QUICK INTEGRATION GUIDE:

- Use `scp` or `sftp` to transfer over the `tar.gz` files from local computer to desired integration server
- Alter config file to reflect that of the production environment. It can be generated with `resilient-circuits config -c`. 
- Sudo into integrations server after SSHing into your profile on `infosec-prod-01.uit.tufts.edu` (`sudo su - integration`)
- NOTE: functions utilizing Python packages must be run on a compatible server (`fn_parse_populate` requires Python3.6+)

```
# pip3.6 install --user fn_x-1.0.0.tar.gz (first time)
pip3.6 install --user --upgrade fn_x-1.0.0.tar.gz
resilient-circuits config -u
resilient-circuits customize
```

- Ensure the function was updated by checking the “Last Modified” timestamp in GUI and using `resilient-circuits list`. 
- AutoPhish contains two functions. This process should be repeated for `fn_parse_populate_pkg-1.0.0.tar.gz` and `fn_query_relate_pkg-1.0.0.tar.gz`, both of which are accessible in the AutoPhish repository. These functions should ultimately be combined in one workflow as shown in the architecture design above. 

USAGE FOR TUFTS INFOSEC OFFICE:

- Already installed on integration server (as of Aug2019)
- sudo into integration server and `resilient-circuits run`
- Menu-Item Rule "AutoPhish trigger" can be executed on incidents with type "Phishing"