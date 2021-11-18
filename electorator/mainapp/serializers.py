from rest_framework import serializers
from accounts.models import Role
from .models import Candidate, Protocol1, Protocol2, Uik, Tik


class ProtocolFirstSerializer(serializers.ModelSerializer):
    """The first protocol"""
    transfer_time = serializers.TimeField(required=False)

    class Meta:
        model = Protocol1
        fields = ['id', 'num_uik', 'num_protocol_1', 'status', 'sum_bul', 'sum_final_bul', 'bad_form', 'transfer_time']

    def get_validation_exclusions(self):
        exclusions = super(ProtocolFirstSerializer, self).get_validation_exclusions()
        return exclusions + ['transfer_time']


class ProtocolSecondSerializer(serializers.ModelSerializer):
    """Creation of the second protocol"""

    class Meta:
        model = Protocol2
        fields = ['num_uik', 'name', 'candidate_votes']


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "party", "info", "photo"]


class UIKSerializer(serializers.ModelSerializer):
    """Read info about uik"""

    class Meta:
        model = Uik
        fields = ["id", "num_uik", "num_tik", "population", "status",
                  "sum_votes", "sum_numb_votes_fin", "presence",
                  "perc_final_bul", "bad_form", "update_time"]


class CandidatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name", "info", "sum_votes"]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["role_user"]


class UikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ["num_uik"]


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ['num_tik', 'presence']


class PresenceSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ['num_tik', 'sum_votes', 'population', 'presence']


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "party", "info", "photo", "sum_votes", "birthday", "birthday_place", "education",
                  "polit_position", "position", "work"]


class TopTikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ['num_tik', 'population']


class TopTikSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Tik
        fields = ['num_tik', 'population']


class TikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tik
        fields = '__all__'
