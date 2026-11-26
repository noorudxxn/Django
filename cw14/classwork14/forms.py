from django import forms

class CertificateForm(forms.Form):
    student_name = forms.CharField(
        max_length=100,
        label="Student Name"
    )

    course_name = forms.CharField(
        max_length=100,
        label="Course Name"
    )

    completion_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Completion Date"
    )

    email = forms.EmailField(
        label="Student Email"
    )