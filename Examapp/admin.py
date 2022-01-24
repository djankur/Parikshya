from django.contrib import admin

# Register your models here.
from .models import Question, Registration, Result, Teacher

admin.site.register(Registration)
admin.site.register(Teacher)
admin.site.register(Question)
admin.site.register(Result)