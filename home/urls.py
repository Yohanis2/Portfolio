
from django.urls import path
from home import views



# django admin changes
#admin.site.site_header = "Login to Burhan"
#admin.site.site_title = "Welocom to DashBord"
#admin.site.index_title = "Welocom to Portal"



urlpatterns = [
    path('home/', views.home, name='home'),
    path('',views.contact, name='contact'),
    path('home2/', views.home2, name='home2'),
    path('detail_contact/<int:pk>', views.detail_contact, name='detail_contact'),
    path('delete_contact/<int:pk>',views.delete_contact ,name='delete_contact'),
    #path('project/', views.project, name='project'), 
]