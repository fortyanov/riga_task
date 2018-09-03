from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from main.bl import NumberHandler, TextHandler
from main.rest.serializers import UsefulNumberSerializer, UsefulTextSerializer


class EndpointView(APIView):
    def __init__(self, *args, **kwargs):
        APIView.__init__(self, *args, **kwargs)
        self.ser_bl_mapper = [
            (UsefulNumberSerializer, NumberHandler),
            (UsefulTextSerializer, TextHandler),
        ]

    def post(self, request, *args, **kwargs):
        for ser_cls, bl_cls in self.ser_bl_mapper:
            ser = ser_cls(data=request.data)
            if ser.is_valid(raise_exception=False):
                bl_result = bl_cls(ser.validated_data).run()
                return Response(data=bl_result, status=HTTP_200_OK)

        return Response(data='Incorrect data format', status=HTTP_400_BAD_REQUEST)
