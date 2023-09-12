from django.shortcuts import render
from .models import Main_detials,Main_details_1,Individual_parts_model
from django.http import HttpResponse
# Create your views here.
def Main_Home_page(request):
    Detail_1=Main_detials()
    Detail_1.name='Circuit_diagram'
    Detail_1.img='Circuit_diagram.jpg'
    
    Detail_2=Main_detials()
    Detail_2.name='MCB_details'
    Detail_2.img='Mcb.jpg'
    
    Detail_3=Main_detials()
    Detail_3.name='Parts_Info'
    Detail_3.img='Individual_parts.jpg'
    
    # Details=[Detail_1,Detail_2,Detail_3]
    Videos_1=Main_details_1()
    Videos_1.name='Product_Video'
    Videos_1.vid='Product_vid.mp4'
    
    Details=[Detail_1,Detail_2,Detail_3]
    Videos=Videos_1
    
    context={'Details': Details, 'Videos': Videos}
    # return render(request,'Internal_detials/Main_Page.html',{'Details':Details})
    return render(request,'Internal_detials/Main_Page.html',context)


def MCB_pdf_view(request):
    pdf_url='static/Internal_detials/pdf/MCB-Boek-2016-11edruk.pdf'
    with open(pdf_url,'rb') as pdf:
        response=HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition']='inline;filename=MCB-Boek-2016-11edruk.pdf'
        return response
    
def Circuit_details(request):
    pdf_url='static/Internal_detials/pdf/CircuitDrawingsandWiring.pdf'
    with open(pdf_url,'rb') as pdf:
        response=HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition']='inline;filename=CircuitDrawingsandWiring.pdf'
        return response
    
def Video_details(request):
    context={'user':'Happy'}
    return True

def Individual_details(request):
    Part_1=Individual_parts_model()
    Part_1.name='Extinguisher'
    Part_1.img='Extinguisher.jpg'
    
    Part_2=Individual_parts_model()
    Part_2.name='Actuator'
    Part_2.img='Actuator.jpg'
    
    Part_3=Individual_parts_model()
    Part_3.name='Mounting_lock'
    Part_3.img='Mounting_lock.jpg'
    
    Parts=[Part_1,Part_2,Part_3]
    return render(request,'Internal_detials/Individual_Parts.html',{'Parts':Parts})
