# Create your views here.
from django.template import RequestContext, Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from models import WebDesigner
from form import sanitizeUrl, AddNewDesignerForm, SearchWebsiteForm

def home_page(request):
    return render_to_response("home.html",
            context_instance=RequestContext(request))

def thankyou_page(request):
    return render_to_response("thankyou.html",
            context_instance=RequestContext(request))
    
def results_page(request):
    return render_to_response("results.html",
            context_instance=RequestContext(request))
                    
def search_designer(request):
    website = request.GET.get('website', '')
    website = sanitizeUrl(website)
    if website:
	results = WebDesigner.objects.filter(website_designed = website)
    	return render_to_response("results.html",{'results':results},context_instance=RequestContext(request))
    else:
	return render_to_response('home.html',context_instance=RequestContext(request))
	
def AddDesigner(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AddNewDesignerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            clean = form.cleaned_data
            developer = WebDesigner(designer=clean['name'],designer_url=clean['designer_url'],website_designed = clean['website_designed'])
            developer.save()
            return HttpResponseRedirect("thanks") # Redirect after POST
    else:
        form = AddNewDesignerForm() # An unbound form

    return render_to_response("Add_New_Designer.html", {'form': form,},
                              context_instance=RequestContext(request))