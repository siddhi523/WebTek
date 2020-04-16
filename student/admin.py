from django.contrib import admin

# Register your models here.

from django.db import models
from .models import Board
admin.site.register(Board)
