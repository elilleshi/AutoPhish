# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_parse_populate_pkg"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_parse_populate_pkg package"""
    reload_params = {"package": u"fn_parse_populate_pkg",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"attachment_id", u"incident_id"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_autophish"], 
                    "functions": [u"fn_parse_populate"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [],
                    "actions": [],
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     attachment_id
    #     incident_id
    #   Message Destinations:
    #     fn_autophish
    #   Functions:
    #     fn_parse_populate


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMiwgIm1pbm9yIjogMSwgImJ1aWxkX251bWJl
ciI6IDkzLCAidmVyc2lvbiI6ICIzMi4xLjkzIn0sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAy
LCAiaWQiOiAyOCwgImV4cG9ydF9kYXRlIjogMTU2MzIxMTk1NjAwMiwgImZpZWxkcyI6IFt7Imlk
IjogMzgsICJuYW1lIjogImluY190cmFpbmluZyIsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAicHJl
Zml4IjogbnVsbCwgInR5cGVfaWQiOiAwLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVu
dCBpcyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiBUaGlzIGZpZWxkIGlzIHJl
YWQtb25seS4iLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImhpZGVfbm90aWZpY2F0aW9uIjog
ZmFsc2UsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNl
LCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnRlcm5hbCI6IGZhbHNlLCAidXVpZCI6ICJjM2Yw
ZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EiLCAib3BlcmF0aW9ucyI6IFtdLCAib3Bl
cmF0aW9uX3Blcm1zIjoge30sICJ2YWx1ZXMiOiBbXSwgInJlYWRfb25seSI6IHRydWUsICJjaGFu
Z2VhYmxlIjogdHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVu
dC9pbmNfdHJhaW5pbmciLCAidGVtcGxhdGVzIjogW10sICJkZXByZWNhdGVkIjogZmFsc2UsICJj
YWxjdWxhdGVkIjogZmFsc2V9LCB7ImlkIjogMTAxNCwgIm5hbWUiOiAiYXR0YWNobWVudF9pZCIs
ICJ0ZXh0IjogImF0dGFjaG1lbnRfaWQiLCAicHJlZml4IjogbnVsbCwgInR5cGVfaWQiOiAxMSwg
InRvb2x0aXAiOiAiIiwgInBsYWNlaG9sZGVyIjogIiIsICJpbnB1dF90eXBlIjogIm51bWJlciIs
ICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2No
b3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwi
OiBmYWxzZSwgInV1aWQiOiAiMTY3NzcxNmEtYTk1ZS00ZjU1LThlM2UtNTM5OWU2ZDNiZDk2Iiwg
Im9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJy
ZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2Us
ICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vYXR0YWNobWVudF9pZCIsICJ0ZW1wbGF0ZXMiOiBb
XSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZX0sIHsiaWQiOiAxMDM0
LCAibmFtZSI6ICJpbmNpZGVudF9pZCIsICJ0ZXh0IjogImluY2lkZW50X2lkIiwgInByZWZpeCI6
IG51bGwsICJ0eXBlX2lkIjogMTEsICJ0b29sdGlwIjogIiIsICJwbGFjZWhvbGRlciI6ICIiLCAi
aW5wdXRfdHlwZSI6ICJudW1iZXIiLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgImhpZGVfbm90aWZp
Y2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZl
ciI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnRlcm5hbCI6IGZhbHNlLCAidXVp
ZCI6ICI4MTFlOTlkNy1kMTk0LTRjZTgtODZjYy1hZmY1ZTAxYWI4NWMiLCAib3BlcmF0aW9ucyI6
IFtdLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ2YWx1ZXMiOiBbXSwgInJlYWRfb25seSI6IGZh
bHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXki
OiAiX19mdW5jdGlvbi9pbmNpZGVudF9pZCIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQi
OiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZX1dLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRh
dGVfZGF0ZSI6IDE1NjMyMTE5NTkyNDUsICJjcmVhdGVfZGF0ZSI6IDE1NjMyMTE5NTkyNDUsICJ1
dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlv
biI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJD
dXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9u
IFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2Us
ICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgInBoYXNlcyI6
IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJvdmVycmlkZXMiOiBbXSwgIm1lc3NhZ2VfZGVz
dGluYXRpb25zIjogW3sibmFtZSI6ICJmbl9hdXRvcGhpc2giLCAicHJvZ3JhbW1hdGljX25hbWUi
OiAiZm5fYXV0b3BoaXNoIiwgImRlc3RpbmF0aW9uX3R5cGUiOiAwLCAiZXhwZWN0X2FjayI6IHRy
dWUsICJ1c2VycyI6IFsiZWxpcmlhbmEubGxlc2hpQHR1ZnRzLmVkdSIsICJyZXN1c2VyQHR1ZnRz
LmVkdSJdLCAidXVpZCI6ICJmZGRjMDc3Ni02NjAxLTQ5NjAtOTFlNS1mZGVkMmQyODA2NmEiLCAi
ZXhwb3J0X2tleSI6ICJmbl9hdXRvcGhpc2gifV0sICJhY3Rpb25zIjogW10sICJsYXlvdXRzIjog
W10sICJub3RpZmljYXRpb25zIjogbnVsbCwgInRpbWVmcmFtZXMiOiBudWxsLCAibG9jYWxlIjog
bnVsbCwgImluZHVzdHJpZXMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJnZW9zIjogbnVs
bCwgInRhc2tfb3JkZXIiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAidHlwZXMiOiBbXSwgInNj
cmlwdHMiOiBbXSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJ3b3JrZmxvd3MiOiBb
XSwgInJvbGVzIjogW10sICJ3b3Jrc3BhY2VzIjogW10sICJmdW5jdGlvbnMiOiBbeyJpZCI6IDky
LCAibmFtZSI6ICJmbl9wYXJzZV9wb3B1bGF0ZSIsICJkaXNwbGF5X25hbWUiOiAiUGFyc2UgYW5k
IFBvcHVsYXRlIiwgImRlc2NyaXB0aW9uIjogeyJmb3JtYXQiOiAidGV4dCIsICJjb250ZW50Ijog
IlBhcnNlcyBhbiBpbmNpZGVudCdzIC5lbWwgZmlsZSBhdHRhY2htZW50IChmb3J3YXJkZWQgZW1h
aWwpIGFuZCBwb3B1bGF0ZXMgdGhlIGluY2lkZW50IHdpdGggYXJ0aWZhY3RzIGdpdmVuIHRoZSBp
bmZvcm1hdGlvbiB3aXRoaW4gdGhlIGZpbGUuIn0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5f
YXV0b3BoaXNoIiwgImV4cG9ydF9rZXkiOiAiZm5fcGFyc2VfcG9wdWxhdGUiLCAidXVpZCI6ICJj
YWRkZDhjOC0wYjY5LTQ1OGEtYjI2NS00NWQ4MjEzZGZjZTQiLCAidmVyc2lvbiI6IDMsICJjcmVh
dG9yIjogeyJpZCI6IDM2LCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAiZWxpcmlhbmEubGxlc2hp
QHR1ZnRzLmVkdSIsICJkaXNwbGF5X25hbWUiOiAiRWxpcmlhbmEgTGxlc2hpIn0sICJsYXN0X21v
ZGlmaWVkX2J5IjogeyJpZCI6IDMsICJ0eXBlIjogInVzZXIiLCAibmFtZSI6ICJyZXN1c2VyQHR1
ZnRzLmVkdSIsICJkaXNwbGF5X25hbWUiOiAiUmVzIFVzZXIifSwgImxhc3RfbW9kaWZpZWRfdGlt
ZSI6IDE1NjI5Mzc2OTMwNjgsICJ2aWV3X2l0ZW1zIjogW3sic3RlcF9sYWJlbCI6IG51bGwsICJz
aG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9f
ZnVuY3Rpb24iLCAiY29udGVudCI6ICI4MTFlOTlkNy1kMTk0LTRjZTgtODZjYy1hZmY1ZTAxYWI4
NWMiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlfSwgeyJzdGVwX2xhYmVsIjogbnVsbCwgInNo
b3dfaWYiOiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19m
dW5jdGlvbiIsICJjb250ZW50IjogIjE2Nzc3MTZhLWE5NWUtNGY1NS04ZTNlLTUzOTllNmQzYmQ5
NiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9XSwgIndvcmtmbG93cyI6IFt7IndvcmtmbG93
X2lkIjogMTAzLCAibmFtZSI6ICJQYXJzZStQb3B1bGF0ZSIsICJwcm9ncmFtbWF0aWNfbmFtZSI6
ICJwYXJzZXBvcHVsYXRlIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgImRlc2NyaXB0aW9u
IjogbnVsbCwgInV1aWQiOiBudWxsLCAiYWN0aW9ucyI6IFtdfV19XX0=
"""
    )