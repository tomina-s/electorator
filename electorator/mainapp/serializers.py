from rest_framework import serializers
# from .models import DB_test
from .models import Candidate


class DB_testSerializer(serializers.ModelSerializer):
    class Meta:
        pass


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

