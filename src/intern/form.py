from django import forms
import re, sys, string


class AddNewDesignerForm(forms.Form):
    name = forms.CharField(max_length=100)
    designer_url = forms.URLField(max_length=100)
    website_designed = forms.URLField(max_length=100)
  
class SearchWebsiteForm(forms.Form):
    website_designed = forms.CharField(max_length=100)
        
def sanitizeUrl(website, Strict=None):

    # strings = re.split(r"([^\-a-zA-Z0-9_]+)",link)[:-1]
    strings = re.split(r"([^\-a-zA-Z0-9_]+)",website)

    if not strings:
        return None
    
    if strings[0] == "http":
        if strings[1] == "://":
            if Strict:                
                if "." in strings[2:]:
                    return "".join(strings[2:])  # it's valid!
            else:
                return "".join(strings[2:])
    else:
        return website