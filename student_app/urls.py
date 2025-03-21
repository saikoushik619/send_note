from django.urls import path
from . import views
urlpatterns=[

    path('populate/',views.upload_data),
    path('detailsdisplay/',views.fetch_student_display),
    path('locations/',views.fetch_student_locations),
    #path('locations/',views.fetch_locations),
    #path('totaldetails',views.total_student_display),
    path('singleregion/<str:student_location>/',views.single_region_students),
    path('selected_students/',views.selected_students_display,name='selected_students_url'),
    path('selected_rows/',views.program_info_save),
    path('student_details/',views.all_student_details),
    path('student_reports/',views.program_info_display,name='student_report_url'),
    path('student_report_send/',views.program_info_details),
    path('program_report/',views.program_report,name='programDetails'),
    path('campaignDetails/',views.campaign_details_display)


]