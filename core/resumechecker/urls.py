from django.urls import path
from . import views

urlpatterns = [
    path("jobs/",views.JobDescriptionView.as_view(),name="Jobdescription"),
    path("resumes/",views.AnalyzeResumeView.as_view())
]