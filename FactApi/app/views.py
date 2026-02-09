from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import *
# Create your views here.

class FactCRUD(APIView):
    def get(self,request,pk=None):
        if pk == None:
            FTO=Fact.objects.all()                   
            FJD=FactMS(FTO,many=True)                
            return Response(FJD.data)                  
        else:
            FO=Fact.objects.get(id=pk)   
            FJD=FactMS(FO)    
            return Response(FJD.data)  


    def post(self,request):
        FJDO=request.data 
        PO=FactMS(data=FJDO)
        if PO.is_valid(): 
            PO.save() 
            return Response({"msg":"Fact Created"})
        return Response(PO.errors)
    
    def put(self,request,pk):ta
        FJDO=request.data                                
        FO=Fact.objects.get(id=pk)                   
        PO=FactMS(FO,data=FJDO)                      
        if PO.is_valid():                               
            PO.save()                                   
            return Response({"msg":"Fact Updated"})     
        return Response(PO.errors)

    def patch(self,request,pk):
        FJDO=request.data                                  
        FO=Fact.objects.get(id=pk)                     
        PO=FactMS(FO,data=FJDO,partial=True)             
        if PO.is_valid():                                   
            PO.save()                                      
            return Response({"msg":"Fact Partially Updated"})        
        return Response(PO.errors)

    def delete(self,request,pk):
        PO=Fact.objects.get(id=pk)                       
        PO.delete()                                        
        return Response({"msg":"Fact Deleted"})         

    
        
