# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_query_relate_pkg"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_query_relate_pkg package"""
    reload_params = {"package": u"fn_query_relate_pkg",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"incident_id"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_autophish"], 
                    "functions": [u"fn_query_relate"], 
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
    #     incident_id
    #   Message Destinations:
    #     fn_autophish
    #   Functions:
    #     fn_query_relate


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMiwgIm1pbm9yIjogMSwgImJ1aWxkX251bWJl
ciI6IDkzLCAidmVyc2lvbiI6ICIzMi4xLjkzIn0sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAy
LCAiaWQiOiAyNywgImV4cG9ydF9kYXRlIjogMTU2MTkwOTA1NzAyMywgImZpZWxkcyI6IFt7Imlk
IjogMzIwLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAidGV4dCI6ICJTaW11bGF0aW9uIiwgInBy
ZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMCwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRl
bnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMg
cmVhZC1vbmx5LiIsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFs
c2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogImMz
ZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJvcGVyYXRpb25zIjogW10sICJv
cGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogdHJ1ZSwgImNo
YW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lk
ZW50L2luY190cmFpbmluZyIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwg
ImNhbGN1bGF0ZWQiOiBmYWxzZX0sIHsiaWQiOiAxMTY4LCAibmFtZSI6ICJpbmNpZGVudF9pZCIs
ICJ0ZXh0IjogImluY2lkZW50X2lkIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMTEsICJ0
b29sdGlwIjogIiIsICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAi
cmVxdWlyZWQiOiAiYWx3YXlzIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4i
OiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiYmxhbmtfb3B0aW9u
IjogZmFsc2UsICJpbnRlcm5hbCI6IGZhbHNlLCAidXVpZCI6ICI4MTFlOTlkNy1kMTk0LTRjZTgt
ODZjYy1hZmY1ZTAxYWI4NWMiLCAib3BlcmF0aW9ucyI6IFtdLCAib3BlcmF0aW9uX3Blcm1zIjog
e30sICJ2YWx1ZXMiOiBbXSwgInJlYWRfb25seSI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUs
ICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9pbmNpZGVudF9p
ZCIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBm
YWxzZX1dLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1NjE5MDkwNjA2MjMs
ICJjcmVhdGVfZGF0ZSI6IDE1NjE5MDkwNjA2MjMsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFl
OC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2th
Z2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChp
bnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAi
ZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlk
ZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgInBoYXNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjog
W10sICJvdmVycmlkZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sibmFtZSI6ICJm
bl9hdXRvcGhpc2giLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZm5fYXV0b3BoaXNoIiwgImRlc3Rp
bmF0aW9uX3R5cGUiOiAwLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsiZWxpcmlhbmEu
bGxlc2hpQHR1ZnRzLmVkdSJdLCAidXVpZCI6ICJmZGRjMDc3Ni02NjAxLTQ5NjAtOTFlNS1mZGVk
MmQyODA2NmEiLCAiZXhwb3J0X2tleSI6ICJmbl9hdXRvcGhpc2gifV0sICJhY3Rpb25zIjogW10s
ICJsYXlvdXRzIjogW10sICJub3RpZmljYXRpb25zIjogbnVsbCwgInRpbWVmcmFtZXMiOiBudWxs
LCAibG9jYWxlIjogbnVsbCwgImluZHVzdHJpZXMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGws
ICJnZW9zIjogbnVsbCwgInRhc2tfb3JkZXIiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAidHlw
ZXMiOiBbXSwgInNjcmlwdHMiOiBbXSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJ3
b3JrZmxvd3MiOiBbXSwgInJvbGVzIjogW10sICJ3b3Jrc3BhY2VzIjogW10sICJmdW5jdGlvbnMi
OiBbeyJpZCI6IDkxLCAibmFtZSI6ICJmbl9xdWVyeV9yZWxhdGUiLCAiZGlzcGxheV9uYW1lIjog
IlF1ZXJ5IGFuZCBSZWxhdGUiLCAiZGVzY3JpcHRpb24iOiB7ImZvcm1hdCI6ICJ0ZXh0IiwgImNv
bnRlbnQiOiAiQ29tcGxldGVzIHRoZSBBdXRvUGhpc2ggd29ya2Zsb3cgYnkgcXVlcnlpbmcgZWFj
aCBhcnRpZmFjdCB3aXRoaW4gdGhlIGVudGlyZSBkYXRhc2V0IG9mIGFydGlmYWN0cywgZXNjYWxh
dGluZyBpbmNpZGVudHMgaWYgbmVjZXNzYXJ5LCBhbmQgcmVsYXRpbmcgaW5jaWRlbnRzIHRvIGVh
Y2ggb3RoZXIgdGhyb3VnaCBhcnRpZmFjdHMuIn0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5f
YXV0b3BoaXNoIiwgImV4cG9ydF9rZXkiOiAiZm5fcXVlcnlfcmVsYXRlIiwgInV1aWQiOiAiMjhh
MjVmOWEtYzcxYS00MjQzLTlhYTUtYTA3MTIzN2FhMTE3IiwgInZlcnNpb24iOiAyLCAiY3JlYXRv
ciI6IHsiaWQiOiAzNiwgInR5cGUiOiAidXNlciIsICJuYW1lIjogImVsaXJpYW5hLmxsZXNoaUB0
dWZ0cy5lZHUiLCAiZGlzcGxheV9uYW1lIjogIkVsaXJpYW5hIExsZXNoaSJ9LCAibGFzdF9tb2Rp
ZmllZF9ieSI6IHsiaWQiOiAzNiwgInR5cGUiOiAidXNlciIsICJuYW1lIjogImVsaXJpYW5hLmxs
ZXNoaUB0dWZ0cy5lZHUiLCAiZGlzcGxheV9uYW1lIjogIkVsaXJpYW5hIExsZXNoaSJ9LCAibGFz
dF9tb2RpZmllZF90aW1lIjogMTU2MTkwODc1ODIxOSwgInZpZXdfaXRlbXMiOiBbeyJzdGVwX2xh
YmVsIjogbnVsbCwgInNob3dfaWYiOiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZp
ZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJjb250ZW50IjogIjgxMWU5OWQ3LWQxOTQtNGNlOC04
NmNjLWFmZjVlMDFhYjg1YyIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9XSwgIndvcmtmbG93
cyI6IFt7IndvcmtmbG93X2lkIjogOTcsICJuYW1lIjogIkF1dG9QaGlzaCIsICJwcm9ncmFtbWF0
aWNfbmFtZSI6ICJhdXRvcGhpc2giLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAiZGVzY3Jp
cHRpb24iOiBudWxsLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW119XX1dfQ==
"""
    )