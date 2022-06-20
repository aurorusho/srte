from django.urls import path
from . import views


app_name = 'written_expression'


urlpatterns = [
    path('', views.select_quantity, name='quantity'),
    path(
        'test/<int:quantity>',
        views.QuestionView.as_view(),
        name = 'questions'
        ),
    path('check/', views.CheckAnswers.as_view(), name='check')
]



