
from .serializer import EmpSerilizer,DepSerilizer
from .models import Employee ,Department 
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class EmpView(APIView):
    def get(self,request):
        employees =Employee.objects.all()
        serilizer =EmpSerilizer(employees,many = True)
        return Response(serilizer.data)
       
    def post(self,request):
        serilizer =EmpSerilizer(data =request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
    def put(self,request,pk):
        employee = Employee.objects.get(id=pk)
        serializer=EmpSerilizer(employee,data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
    def delete(self,request,pk):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({"message":"Employee deleted "})

class DepView(APIView):
    def get(self,request):
        departments = Department.objects.all()
        serializer=DepSerilizer(departments,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=DepSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def put(self,request,pk):
        department = Department.objects.get(id=pk)
        serializer=DepSerilizer(department,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk):
        department = Department.objects.get(id=pk)
        department.delete()
        return Response({"message":"Department deleted"})