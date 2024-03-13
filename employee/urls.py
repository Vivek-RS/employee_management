"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (EmployeeUpdateDeleteAPIView, ShiftGetCreateAPIView, EmployeeGetCreateAPIView, TicketGetCreateAPIView,
                    TicketUpdateDeleteAPIView, ShiftUpdateDeleteAPIView, TicketEmployeesAPIView,UnassignedTicketsAPIView)

urlpatterns = [
    path('employee/<int:pk>/', EmployeeUpdateDeleteAPIView.as_view()),
    path('ticket/<int:pk>/', TicketUpdateDeleteAPIView.as_view()),
    path('shift/<int:pk>/', ShiftUpdateDeleteAPIView.as_view()),
    path('employee/', EmployeeGetCreateAPIView.as_view()),
    path('ticket_dash/', TicketEmployeesAPIView.as_view()),
    path('ticket/', TicketGetCreateAPIView.as_view()),
    path('shift', ShiftGetCreateAPIView.as_view()),
    path('unassigned_tickets/',UnassignedTicketsAPIView.as_view())
]