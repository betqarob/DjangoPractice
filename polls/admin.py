from django.contrib import admin
from .models import Question

# this will allow me to modify the poll app from the admin page
admin.site.register(Question)
