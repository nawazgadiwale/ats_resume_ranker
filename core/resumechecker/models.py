from django.db import models

# Create your models here.
class Resume(models.Model):
    resume = models.FileField(upload_to="resumes/")

class JobDescription(models.Model):
    jobtitle = models.CharField(max_length=100)
    job_description = models.TextField()


    def __str__(self):
        return f"{self.job_description},{self.jobtitle}"