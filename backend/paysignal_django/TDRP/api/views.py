from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from ..models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 


@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer = r_or_l_serilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def login(request):
    request.session['email']=None
    if request.method=='POST':
        email = request.data.get('email')
        password = request.data.get('password')
        permission=Register.objects.get(email=email)
        if password==permission.password:
            request.session['email']=email
            return Response({'message': 'login successfully'},status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','POST'])
def complaints(request):
    if request.method=='GET':
        complaint=transaction_details.objects.filter(email=request.session['email']).order_by('-complaint_date')
        serializer=transaction_details_serilaizer(complaint,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = transaction_details_serilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def admin(request, id=None):
    if request.method=='GET':
        # email = request.data.get('')
        # complaint=transaction_details.objects.all()
        statuses = request.GET.get('status', 'pending')  # Default status is 'pending'
        complaint = transaction_details.objects.filter(status=statuses).order_by('-complaint_date')
        serializer=transaction_details_serilaizer(complaint,many=True)
        return Response(serializer.data)    
    if request.method=='PATCH':
        print(id)
        try:
            complaint = transaction_details.objects.get(id=id)  # Find complaint by ID
        except transaction_details.DoesNotExist:
            return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = transaction_details_update_serilaizer(complaint, data=request.data, partial=True)  # Allow partial update

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print("Validation errors:", serializer.errors)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    