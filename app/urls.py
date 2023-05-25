from django.urls import path
from app import views
urlpatterns = [
    path('',views.erp,name='erp'),
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('subproducts/<str:type>',views.subproducts,name='subproducts'),
    path('productdescription/<int:id>',views.productdescription,name='productdescription'),
    path('projectimages/<str:type>',views.projectimages,name='projectimages'),
    path('projects/',views.projectcategory,name='projects'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),

]
