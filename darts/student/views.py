from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from .serializers import Responses


class StudentViewSet(APIView):
    def get(self, request, id=None):
        res = Responses().api_response()
        try:
            res.update({'data': serializers.getStudentById(request, id)})
        except Exception as e:
            res.update({'success': False, 'code': 500, 'error_string': str(e)})
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res)


class StudentTotalViewSet(APIView):
    def get(self, request):
        res = Responses().api_response()
        try:
            res.update({'data': serializers.getStudentsTotal()})
        except Exception as e:
            res.update({'success': False, 'code': 500, 'error_string': str(e)})
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res)


class SubjectAverageViewSet(APIView):
    def get(self, request):
        res = Responses().api_response()
        try:
            res.update({'data': serializers.getSubjectAverage()})
        except Exception as e:
            res.update({'success': False, 'code': 500, 'error_string': str(e)})
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res)


class GetCacheDf(APIView):
    def get(self, request):
        res = Responses().api_response()
        try:
            res.update({'data': serializers.update_dataframe(request)})
        except Exception as e:
            res.update({'success': False, 'code': 500, 'error_string': str(e)})
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(res)
