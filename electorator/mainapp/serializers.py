"""Mainapp serializer"""
from rest_framework import serializers
from accounts.models import Role
from .models import Candidate, Protocol1, Protocol2, Uik, Tik


class ProtocolFirstSerializer(serializers.ModelSerializer):
    """The first protocol"""
    transfer_time = serializers.TimeField(required=False)

    class Meta:
        # pylint: disable=too-few-public-methods
        """The first protocol fields"""
        model = Protocol1
        fields = ['id', 'num_uik', 'num_protocol_1', 'status', 'sum_bul',
                  'sum_final_bul', 'bad_form', 'transfer_time']

    def get_validation_exclusions(self):
        # pylint: disable=no-member, super-with-arguments
        """Override function"""
        exclusions = super(ProtocolFirstSerializer, self).get_validation_exclusions()
        return exclusions + ['transfer_time']


class ProtocolSecondSerializer(serializers.ModelSerializer):
    """Creation of the second protocol"""

    class Meta:
        # pylint: disable=too-few-public-methods
        """The second protocol fields"""
        model = Protocol2
        fields = ['num_uik', 'name', 'candidate_votes']


class CandidateSerializer(serializers.ModelSerializer):
    """Candidate serializer"""
    class Meta:
        """Candidate serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Candidate
        fields = ["id", "name", "party", "info", "photo"]


class UIKSerializer(serializers.ModelSerializer):
    """Read info about uik"""

    class Meta:
        # pylint: disable=too-few-public-methods
        """UIK serializer fields"""
        model = Uik
        fields = ["id", "num_uik", "num_tik", "population", "status",
                  "sum_votes", "sum_numb_votes_fin", "presence",
                  "perc_final_bul", "bad_form", "update_time"]


class CandidateInfoSerializer(serializers.ModelSerializer):
    """Candidate serializer"""

    class Meta:
        """Candidate serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Candidate
        fields = ["name", "info", "sum_votes"]


class RoleSerializer(serializers.ModelSerializer):
    """Role serializer"""

    class Meta:
        """Role serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Role
        fields = ["role_user"]


class UikSerializer(serializers.ModelSerializer):
    """UIK serializer"""
    class Meta:
        """UIK serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Uik
        fields = ["num_uik"]


class PresenceSerializer(serializers.ModelSerializer):
    """Presence serializer"""
    class Meta:
        """Presence serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Uik
        fields = ['num_tik', 'presence']


class PresenceSerializer1(serializers.ModelSerializer):
    """Presence serializer"""
    class Meta:
        """Presence serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Uik
        fields = ['num_tik', 'sum_votes', 'population', 'presence']


class VotesSerializer(serializers.ModelSerializer):
    """Votes serializer"""
    class Meta:
        """Votes serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Candidate
        fields = ["id", "name", "party", "info", "photo", "sum_votes",
                  "birthday", "birthday_place", "education",
                  "polit_position", "position", "work"]


class TopTikSerializer(serializers.ModelSerializer):
    """TopTik serializer"""

    class Meta:
        """TopTik serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Uik
        fields = ['num_tik', 'population']


class TopTikSerializer1(serializers.ModelSerializer):
    """TopTik serializer"""
    class Meta:
        """TopTik serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Tik
        fields = ['num_tik', 'population']


class TikSerializer(serializers.ModelSerializer):
    """Tik serializer"""
    class Meta:
        """Tik serializer fields"""
        # pylint: disable=too-few-public-methods
        model = Tik
        fields = '__all__'
