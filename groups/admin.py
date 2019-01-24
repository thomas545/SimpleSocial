from django.contrib import admin
from .models import Group, GroupMember
# Register your models here.

class GroupMemberInLine(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)
