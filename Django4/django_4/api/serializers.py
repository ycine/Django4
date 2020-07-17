# from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields

from models import Technologie, rodzaje1, jezyki1

from multiselectfield import MultiSelectField

# class TechnologieSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Technologie
#         fields = ['jezyk', 'biblioteka', 'rodzaj', 'opis','data']


# class TechnologieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Technologie
#         my_field = fields.MultipleChoiceField(choices=rodzaje1) 
#         fields = ['jezyk', 'biblioteka', "rodzaj", 'opis','data'] 



class TechnologieSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    jezyk = serializers.ChoiceField(choices=jezyki1)
    biblioteka = serializers.CharField(max_length=30) 
    rodzaj = fields.MultipleChoiceField(choices=rodzaje1)
    opis = serializers.CharField(max_length=300)
    # data = serializers.DateTimeField() 


    def create(self, validated_data):
        return Technologie.objects.create(**validated_data)

    
    def update(self, Technologie, validated_data):
        Technologie.jezyk = validated_data.get('jezyk', Technologie.jezyk)
        Technologie.biblioteka = validated_data.get('biblioteka', Technologie.biblioteka)
        Technologie.rodzaj = validated_data.get('rodzaj', Technologie.rodzaj)
        Technologie.opis = validated_data.get('opis', Technologie.opis)
        Technologie.save()
        return Technologie


    # class Meta:
    #     model = Technologie
    #     fields = ['id', 'jezyk', 'biblioteka', 'rodzaj', 'opis']
        