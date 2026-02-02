from rest_framework import serializers
from .models import JobDescription,Resume
class JobDescriptionserializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = "__all__"

class ResumeSerializer(serializers.ModelSerializer):
    job_description = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=False
    )

    class Meta:
        model = Resume
        fields = ["resume", "job_description"]

    def create(self, validated_data):
        validated_data.pop("job_description")
        return Resume.objects.create(**validated_data)
