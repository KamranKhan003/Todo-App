from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from loginsystem.forms import SignupForm
from .models import *


# Register User Model
@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    add_form = SignupForm
    fieldsets = (*UserAdmin.fieldsets,('user roll',{'fields':('image',)}))

# Register Todo Model
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
