from django.shortcuts import render
from service_app.models import *
# Create your views here.
def service_about_view(request):
    service_header_content = service_about_heading.objects.all()
    service_area = service_progress_aria.objects.all()
    feature_title_data = feature_title.objects.all()
    service_feature_data = service_feature.objects.all()
    service_contact_data = service_Contact.objects.all()

    context ={'feature_title_data': feature_title_data,
              'service_feature_data': service_feature_data,
              'service_header_content': service_header_content,
              'service_area': service_area,
              'service_contact_data': service_contact_data
              }
                
    
    return render(request, 'webpages/service.html', context)