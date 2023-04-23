from django.urls import path
from . import views
urlpatterns = [
	# path('hello/', views.hello_world, name = 'hello' ),
	path('posts/<int:id>/', views.blog_detail_view, name='detail'),
	path('', views.blog_all, name='posts'),
	path('add-tv/',views.create_post_view, name='create'),
]

