from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from resumechecker.serializer import JobDescriptionserializer,ResumeSerializer
from .models import JobDescription,Resume
from .analyzer import process_resume

class JobDescriptionView(APIView):
    def get(self,request):
        queryset = JobDescription.objects.all()
        serializer = JobDescriptionserializer(queryset,many = True)
        return Response({
            "status" : True,
            "data" : serializer.data

        })

# class AnalyzeResumeView(APIView):
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request):
#         serializer = ResumeSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response(
#                 {"status": False, "data": serializer.errors},
#                 status=400
#             )

#         job_description = serializer.validated_data["job_description"]

#         resume_instance = serializer.save()
#         resume_path = resume_instance.resume.path

#         data = process_resume(
#             resume_path,
#             job_description
#         )

#         return Response({
#             "status": True,
#             "message": "resume analyzed",
#             "data": data
#         })


class AnalyzeResumeView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"status": False, "data": serializer.errors},
                status=400
            )

        job_description = serializer.validated_data["job_description"]

        resume_instance = serializer.save()
        resume_path = resume_instance.resume.path

        analysis = process_resume(resume_path, job_description)

        return Response({
            "status": True,
            "message": "resume analyzed",
            "data": analysis
        })