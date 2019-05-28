from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo_backend_py.note import views

router = routers.DefaultRouter()
router.register(r'note', views.NoteViewSet)


urlpatterns = [
    path('titles/', views.TitleView.as_view()),
    path('note/deleteTestData/', views.delete_test_data),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
