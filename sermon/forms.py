from django import forms 
from .models import Sermon, Review
from django.forms import ModelForm, Textarea

class SermonForm(forms.ModelForm):
  class Meta:
    model = Sermon
    fields = ['title','description','file','thumbnail']
    

class ReviewForm(ModelForm):
  def __init__(self,*args,**kwargs):
    super(ModelForm,self).__init__(*args,**kwargs)
    self.fields['text'].widget.attrs.update({'class':'form-control'})

    
  class Meta:
      model = Review
      fields = ['text']
      labels = {
      
        'text':('Comment'),
      }
      widgets = {
        'text':Textarea(attrs={'rows':4}),
      }
  