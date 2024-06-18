from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserProfile
# Register your models here.
# User = get_user_model()

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', )
    # list_filter = ('created_at',)  #фильтрация по дате создания
    search_fields = ('full_name',)  #создает поисковик по названию



admin.site.register(UserProfile, ProfileAdmin)
