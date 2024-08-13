from django.urls import path
from program import views

urlpatterns=[
    path('prime/<int:num>',views.func1),
    path('anagram/<str:str1>/<str:str2>',views.func2),
    path('square/<int:num>',views.func3),
    path('palin/<int:num>',views.func4),
    path('gcd/<int:n1>/<int:n2>/',views.func5),
]
