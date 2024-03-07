from django.contrib import admin
from .models import CustomUser, TutorialIllustrator, TutorialPhotoshop, Course, Quiz

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(TutorialPhotoshop)
admin.site.register(TutorialIllustrator)
