from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import  action
from api.models import company,employee
from api.serializers import CompanySerializer,employeeserializer
from rest_framework.response import Response

# Create your views here.


## http://127.0.0.1:8000/api/v1/compnaies/{company Id}/employees/

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        
        try:
            cmp=company.objects.get(pk=pk)
            emp=employee.objects.filter(company=cmp)
            emp_serializer=employeeserializer(emp,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({
                'message': 'Compnay might not exist'
            }) 
        
    


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employeeserializer