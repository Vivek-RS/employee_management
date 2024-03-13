from rest_framework import serializers
from employee.models import Employee, Shift, Ticket


class ShiftSerializer(serializers.Serializer):
    SHIFT_CHOICES = (
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
    )
    shift_type = serializers.ChoiceField(choices=SHIFT_CHOICES )
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()

    def create(self, validated_data):
        """
        Create and return a new `Shift` instance, given the validated data.
        """
        return Shift.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        Update and return an existing `Shift` instance, given the validated data.
        """
        instance.shift_type = validated_data.get('shift_type', instance.shift_type)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        return instance


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name=serializers.CharField(required=True, max_length=64)
    last_name=serializers.CharField(required=True, max_length=64)
    joining_date = serializers.DateTimeField()
    is_available = serializers.BooleanField(default=True)
    shift_type = serializers.PrimaryKeyRelatedField(queryset=Shift.objects.all())

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.joining_date = validated_data.get('joining_date', instance.joining_date)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.shift_type = validated_data.get('shift_type', instance.shift_type)
        instance.save()
        return instance
    

class TicketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.CharField(required=True, max_length=50)
    creation_date = serializers.DateTimeField(read_only=True)
    description = serializers.CharField()
    resolution_end_date = serializers.DateTimeField()
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=False)
    

    def create(self, validated_data):
        """
        Create and return a new `Ticket` instance, given the validated data.
        """
        ticket = Ticket.objects.create(**validated_data)
        available_employees = Employee.objects.filter(is_available=True)
        #else return  {}
        if available_employees:
            employee = Employee.objects.filter(is_available=True).first()
            ticket.assigned_to=employee
            ticket.save()
            employee.is_available=False
            employee.save()

        return ticket

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.description = validated_data.get('description', instance.description)
        instance.resolution_end_date = validated_data.get('resolution_end_date', instance.resolution_end_date)
        instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
        return instance