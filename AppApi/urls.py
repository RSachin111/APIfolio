from django.urls import path
from . import views

urlpatterns=[
       path('api/work-experience/', views.WorkExperienceList.as_view(), name="work-experience-list")
]