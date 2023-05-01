from django.contrib import admin
from .models import Answer, Question

# Register your models here.


admin.site.register(
    Answer
)  # add models to the Django admin so that data for those models can be created, deleted, updated and queried through the user interface.
admin.site.register(Question)
