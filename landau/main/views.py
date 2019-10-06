from .models import Balance, Capital
from .serializers import BalanceSerializer, CapitalSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .helper_funcs import save_file


class BalanceViewset(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    model = Balance
    serializer_class = BalanceSerializer


class CapitalViewset(viewsets.ModelViewSet):
    queryset = Capital.objects.all()
    model = Capital
    serializer_class = CapitalSerializer

class ExcelViewset(APIView):
    queryset = Capital.objects.none()


    def post(self, request, *args, **kwargs):
        f = request.FILES['file']
        save_file(f)
        print("ASD!!!!!!!!2222222222222222222222222222222222")
        # data = {'salem': 'from_server'}
        return Response({'status': 'ok'})
        # print("asdasdasdasdasd")
