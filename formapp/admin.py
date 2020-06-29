from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from formapp.models import Question
from django.contrib.auth.models import User

# admin.site.unregister(User)

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    pass

# @admin.register(User)
# class UserAdmin(ImportExportModelAdmin):
#     pass