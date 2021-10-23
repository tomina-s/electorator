"""This view provides handlers for configs information"""
from datetime import datetime

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

        return Response(
            {
                'timeToOpen': int(
                    datetime.strptime("23/10/2021-23:55:00", "%d/%m/%Y-%H:%M:%S").timestamp()
                ),
            },
            status=status.HTTP_200_OK
        )
