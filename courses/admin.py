from django.contrib import admin
from .models import Course, Tag, Prerequisite, Learning
from courses.models.video_model import Video
from courses.models.payment import Payment
from courses.models.user_course import UserCourse
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]
admin.site.register(Course, CourseAdmin)

admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment)

