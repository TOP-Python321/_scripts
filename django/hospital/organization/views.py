from django.shortcuts import render
from django.views.generic import ListView, DetailView

from organization import models


class AllDepartments(ListView):
    model = models.Department

