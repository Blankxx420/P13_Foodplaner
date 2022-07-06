from django.contrib import admin
from users.models import User
""" adding User model to admin"""
admin.site.register(User)
