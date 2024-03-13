from employee.models import Employee, Shift, Ticket
from employee.serializers import EmployeeSerializer,ShiftSerializer, TicketSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response("Success", status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

class EmployeeGetCreateAPIView(APIView):
    """
    get, create, update and delete employee
    """
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

class ShiftGetCreateAPIView(APIView):
    """
    get, create, update and delete shift
    """
    def get(self, request):
        shift = Shift.objects.all()
        serializer = ShiftSerializer(shift, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShiftUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        shift = Shift.objects.get(id=pk)
        serializer = ShiftSerializer(instance=shift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            shift = Shift.objects.get(id=pk)
            shift.delete()
            return Response("Success", status=status.HTTP_200_OK)
        except Shift.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
    
class TicketGetCreateAPIView(APIView):
    """
    get, create, update and delete ticket
    """
    def get(self, request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.data == {} return response ticket created no employee to be assigned
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    

class TicketUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            ticket = Ticket.objects.get(id=pk)
            ticket.delete()
            return Response("Success", status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        
class TicketEmployeesAPIView(APIView):
    """
    """
    def get(self, request):
        tickets = Ticket.objects.all()
        response_list = []
        for ticket in tickets:
            response_dict = {}
            response_dict["employee_name"] = ticket.assigned_to.first_name
            response_dict["shift_type"] = ticket.assigned_to.shift_type.shift_type
            response_dict["start_time"] = ticket.assigned_to.shift_type.start_time
            response_dict["end_time"] = ticket.assigned_to.shift_type.end_time
            response_dict["availability_status"] = ticket.assigned_to.is_available
            response_list.append(response_dict)
        return Response(response_list)

class UnassignedTicketsAPIView(APIView):
    """
    """
    def get(self, request):
        ticket = Ticket.objects.filter(assigned_to = None)
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)
