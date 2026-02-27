from django import forms
from .models import Student
from datetime import date

class StudentForm(forms.ModelForm):

    skills = forms.MultipleChoiceField(
        choices=Student.SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect,
            'mode': forms.RadioSelect,
            'address': forms.Textarea(attrs={'rows': 3}),
            'about': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if len(name) < 3:
            raise forms.ValidationError("Full name must have at least 3 characters")
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Mobile number must contain exactly 10 digits")
        return mobile

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob > date.today():
            raise forms.ValidationError("Date of birth cannot be a future date")
        return dob

    def clean_resume(self):
        resume = self.cleaned_data['resume']
        if not resume.name.endswith(('.pdf', '.doc', '.docx')):
            raise forms.ValidationError("Only PDF or DOC files are allowed")
        return resume

    def clean_agree(self):
        agree = self.cleaned_data['agree']
        if not agree:
            raise forms.ValidationError("You must agree to the terms")
        return agree
