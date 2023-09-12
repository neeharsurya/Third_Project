from django.urls import path
from . import views

urlpatterns = [
    path('',views.Main_Home_page,name="Main_Home_Page"),
    path('MCB_details/',views.MCB_pdf_view,name='MCB_details'),
    path('Circuit_diagram/',views.Circuit_details,name='Circuit_diagram'),
    path('Parts_Info/',views.Individual_details,name='Parts_Info'),
]