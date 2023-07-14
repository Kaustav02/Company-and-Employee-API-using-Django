from rest_framework import serializers
from api.models import company,employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model = company
        fields="__all__"
        

class employeeserializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = employee
        fields="__all__"