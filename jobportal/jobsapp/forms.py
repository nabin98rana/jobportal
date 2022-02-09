from django import forms

from jobsapp.models import Job, Applicant

class CreateJobForm(forms.ModelForm):
    """docstring for CreateJobForm."""
    class Meta:
        model = Job
        exclude = ('user', 'created_at')

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job =super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job

class ApplyJobForm(forms.ModelForm):
    """docstring for ApplyJobForm."""
    class Meta:
        model = Applicant
        fields = ('job', )
