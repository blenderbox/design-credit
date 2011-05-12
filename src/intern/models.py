from django.db import models
from form import sanitizeUrl

# Create your models here.
class WebDesigner(models.Model):
    designer = models.CharField(max_length=100)
    designer_url = models.CharField(max_length=100)
    website_designed = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.designer = self.designer
        self.designer_url = sanitizeUrl(self.designer_url)
        self.website_designed = sanitizeUrl(self.website_designed)
        super(WebDesigner, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return  "Website designed:'%s', Designer:'%s', Designer's url: '%s'"%(self.website_designed,
                                                                            self.designer,
                                                                            self.designer_url)