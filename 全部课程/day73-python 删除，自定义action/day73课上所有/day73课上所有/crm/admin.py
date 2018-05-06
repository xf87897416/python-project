from django.contrib import admin
from django.shortcuts import render

from crm import models
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','qq','name','source','consultant','content','status','date')
    list_filter = ('source','consultant','date')
    search_fields = ('qq','name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    list_editable = ('status',)
    list_per_page = 5
    #ordering =


    # actions = ["test_action", ]
    #
    #
    # def test_action(self,request,arg2):
    #     print('test action:',self,request,arg2)
    #     return render(request,"king_admin/table_index.html")
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name')





admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.CourseRecord)
admin.site.register(models.Branch)
admin.site.register(models.Role)
admin.site.register(models.Payment)
admin.site.register(models.StudyRecord)
admin.site.register(models.Tag)
admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.Menu)
