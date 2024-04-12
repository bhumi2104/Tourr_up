from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('fpswd', views.fpswd, name='fpswd'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('set_pswd', views.set_pswd, name='set_pswd'),
    path('seller_index', views.seller_index, name='seller_index'),
    path('change_pswd', views.change_pswd, name='change_pswd'),
    path('our_services', views.our_services, name='our_services'),
    path('about_seller', views.about_seller, name='about_seller'),
    path('add_packages', views.add_packages, name='add_packages'),
    path('package_details/<int:pk>', views.package_details, name='package_details'),
    path('update_package/<int:pk>', views.update_package, name='update_package'),
    path('delete_package/<int:pk>', views.delete_package, name='delete_package'),
    path('all_packages', views.all_packages, name='all_packages'),
    path('customer_inq', views.customer_inq, name='customer_inq'),
    path('about_package/<int:pk>', views.about_package, name='about_package'),
    path('send_inquery/<int:pk>', views.send_inquery, name='send_inquery'),
    path('more_images/<int:pk>', views.more_images, name='more_images'),
    path('my_packages', views.my_packages, name='my_packages'),
    path('add_to_my_packages/<int:pk>',
         views.add_to_my_packages, name='add_to_my_packages'),
    path('remove_from_my_packages/<int:pk>',
         views.remove_from_my_packages, name='remove_from_my_packages'),
    path('success', views.success, name='success'),
    path('deploy/', views.deploy, name='deploy'),
]
