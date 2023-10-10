from django import forms
from .models import Projects,Review

class addProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        widgets = {
            'tag': forms.CheckboxSelectMultiple,      
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields  = ['body',]


    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder':'Enter your text...'})
