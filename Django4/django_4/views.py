from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Technologie
from django_4.serializers import TechnologieSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

def strona_glowna(request):
    return HttpResponse("<h1>Witam w REST !</h1>")


def strona_glowna2(request):
    return render(request, 'index.html')


class TechnologieViewSet2(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Technologie.objects.all()
    serializer_class = TechnologieSerializer



class TechnologieViewSet(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index2.html'

    def get(self, request):
        queryset = Technologie.objects.all()
        # serializer_class = TechnologieSerializer
        return Response({'jezyki':queryset})


    def post(self, request, pk):
        technolog = get_object_or_404(Technologie, pk=pk)
        serializer = TechnologieSerializer(technolog, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': technolog})
        serializer.save()
        return redirect('index2.html')



'''

i started to learn python at my studies, 
but i did`nt learn much at this time. 
I  came back to python when i started my work at ASC in Torun
from this time i learn python almost every day
for diffrent purposes, it really depends on my demands
finally i have reached to Django and because i`m in most cases
concerned with maps ang other geograpical aspects to Geodjango
i made few web based map aplication  but none is utilized by anyone
at this moment.

'''
