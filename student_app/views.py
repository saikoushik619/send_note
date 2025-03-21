

from django.shortcuts import render
from faker import Faker
import random
from django.http import HttpResponse,JsonResponse
from .models import StudentDetails, Location, PhoneNumber, ProgramInfo, CampaignDetails
from.forms import ProgramInfoForm
from model_bakery import baker
import random
status=['delivered','processing','not delivered','rejected']
#POPULATE THE DATA
total_std_details=[]
def upload_data(request):
    faker=Faker()
    regions_list =['missouri','florida','charlotte','texas','chicago',
                   'washington','dallas','mountana','cleveland','tornato']


    for state in regions_list:
        baker.make(Location, region=state)



    for i in range(101):
        std_name=faker.name()
        std_location=random.choice(regions_list)
        std_phn_number=faker.phone_number()
        student_phone_number = ''.join(filter(str.isdigit,std_phn_number))[:10]

        location_instance = Location.objects.get(region = std_location)
        masked_phone_number = masked(student_phone_number)

        create_details = baker.make(StudentDetails,
                                    student_name=std_name,
                                    student_location=location_instance,
                                    masked_number=masked_phone_number)
        create_details.save()

        phone_number_instance=baker.make(PhoneNumber,student_info=create_details,mobile_number=student_phone_number)
        phone_number_instance.save()



        populated_details={
                'student_name':create_details.student_name,
                'student_location':create_details.student_location.region,
                'student_phone_number': create_details.masked_number

            }
        total_std_details.append(populated_details)
    return JsonResponse({'all_details':total_std_details})
# to display phone number in masked

# To display details in html
def fetch_student_display(request):
    return render(request,'student_details_display.html')

# FETCH ALL STUDENT location DETAILS.
def fetch_student_locations(request):

    all_student_locations = Location.objects.all()
    all_student_locations=[ {'name':student_locations.region,
                             'id':student_locations.id
                             } for student_locations in all_student_locations]

    #print(57,all_student_locations)

    return JsonResponse({'available_locations':all_student_locations})


# to get only single region students
def single_region_students(request,student_location):
    if request.method=='GET':
        page_size = request.GET.get('page_size', 10)
        if student_location == 'allLocations':

            total_details = StudentDetails.fetch_student_details()

            print(list(total_details))
            return JsonResponse({'student_data':list(total_details),'page_size':page_size})

        selected_region_students=StudentDetails.fetch_single_region_students(student_location)
        #print(56,selected_region_students)

        #print(59,same_location_students)
        return JsonResponse({'student_data':list(selected_region_students),'page_size':page_size})

           
    return HttpResponse('invalid')


def selected_students_display(request):
    return render(request,'selectedStudents.html')


def program_info_save(request):
    if request.method =='POST':
        #form Validation
        program_info_form=ProgramInfoForm(request.POST, request.FILES)
        if not program_info_form.is_valid() :
            print(104,program_info_form.errors)
        if program_info_form.is_valid() :


            program_name=program_info_form.cleaned_data['program_name']
            selected_ids=program_info_form.cleaned_data['selectedIds']
            program_message=program_info_form.cleaned_data['program_message']
            program_document=program_info_form.cleaned_data['program_document']

            selected_ids = selected_ids.split(",")


            saved_program=ProgramInfo.program_info_save(
                program_name=program_name,
                selected_ids=selected_ids,
                program_message=program_message,
                program_document=program_document)

            response_data={'program_name':saved_program.program_name,
                           'student_count':saved_program.student_count,
                           'program_message':saved_program.program_message,
                           }

            campaign_details_data=CampaignDetails.save_campaign_details(saved_program,selected_ids)

            print(127,campaign_details_data[0].__dict__)

            return JsonResponse({'program_info':response_data})


        else:
            # return HttpResponse('data is not valid')
            return HttpResponse(program_info_form.errors)


def all_student_details(request):
    page_size = request.GET.get('page_size', 10)
    total_details = StudentDetails.fetch_student_details()

    #print(141,list(total_details))
    return JsonResponse({'student_data':list(total_details), 'page_size': page_size})


def program_info_display(request):
    return render(request,'student_report.html')

def program_info_details(request):
    program_details=ProgramInfo.program_info_display()

    return JsonResponse({'data':list(program_details)})


def program_report(request):
    return render(request,'program_details.html')


def campaign_details_display(request):
    campaign_details=CampaignDetails.save_campaign_details()
    return JsonResponse({'data':campaign_details})

#masked
def masked(phone):
    s=''
    for i in range(0,len(phone)):
        if i%2==0:
            s=s+'x'
        else:
            s=s+phone[i]
    return s
