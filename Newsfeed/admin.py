from django.contrib import admin
from Newsfeed.models import *
admin.site.register(comment)
admin.site.register(ratings)
admin.site.register(lesson)
admin.site.register(course)
admin.site.register(People)
admin.site.register(PeopleCourse)
admin.site.register(recommendedList)