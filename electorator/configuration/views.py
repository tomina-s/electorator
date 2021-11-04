"""This view provides handlers for configs information"""
import os
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ConfigAPIView(APIView):
    """config api"""
    permission_classes = [AllowAny]

    @staticmethod
    def get(_):
        """config handler"""
        firstConference = datetime.strptime(os.getenv("FIRST_CONFERENCE", "4/11/2021-23:55:00"), "%d/%m/%Y-%H:%M:%S")
        secondConference = firstConference + timedelta(hours=2)
        thirdConference = firstConference + timedelta(hours=11)

        return Response(
            {
                'timeToOpen': int(
                    datetime.strptime(os.getenv("TIME_TO_OPEN", "27/10/2021-23:55:00"), "%d/%m/%Y-%H:%M:%S").timestamp()
                ),
                'firstConference': int(firstConference.timestamp()),
                'secondConference': int(secondConference.timestamp()),
                'thirdConference': int(thirdConference.timestamp()),
            },
            status=status.HTTP_200_OK
        )
