from django.test import TestCase,Client
from .models import StudentDetails, Location, PhoneNumber, ProgramInfo,CampaignDetails
from . forms import ProgramInfoForm

# Create your tests here.
class StudentTest(TestCase):
    def setUp(self):
        location_instance = Location.objects.create(region='missouri')
        self.dummy=StudentDetails.objects.create(student_name='koushik',student_location=location_instance,
                                             masked_number='0998967878')
    def tests_data(self):
        self.assertEqual(self.dummy.student_name,'koushik')
        with self.assertRaises(AssertionError):
            self.assertNotEqual(self.dummy.student_name, 'koushik')
            self.assertEqual(self.dummy.student_location,'hyderabad')


class PhoneTest(TestCase):
    def setUp(self):
        self.dummy=PhoneNumber.objects.create(mobile_number='9089384098')
    def tests_phone_number(self):
        self.assertEqual(self.dummy.mobile_number,'9089384098')
        self.assertNotEqual(self.dummy.mobile_number,'1234456098')


class LocationTest(TestCase):
    def setUp(self):
        self.dummy=Location.objects.create(region='missouri')
    def test_location(self):
        url='/student/locations/'
        resp=self.client.get(url)
        response=resp.json()
        self.assertEqual(resp.status_code,200)
        self.assertEqual(response['available_locations'][0]['name'], 'missouri')
        self.assertEqual(response['available_locations'][0]['name'], 'missouri')


class Specific_Region_Test(TestCase):
    def setUp(self):
        location_instance = Location.objects.create(region='missouri')
        self.dummy = StudentDetails.objects.create(student_name='koushik', student_location=location_instance,
                                                   masked_number='0998967878')
    def tests_student(self):
        url=f'/student/singleregion/{self.dummy.student_location}/'
        resp=self.client.get(url)
        response=resp.json()
        self.assertEqual(resp.status_code,200)
        self.assertNotEqual(self.dummy.student_location,response['student_data'][0]['student_location'])
        self.assertEqual(self.dummy.student_name, response['student_data'][0]['student_name'])

#Model TestCase
class ProgramInfoTest(TestCase):
    def test_ProgramInfo(self):
        program_details=ProgramInfo.objects.create(program_name='AnnualDay',
                                                   student_count=2,
                                                   program_message='hello'
                                                   )
        self.assertEqual(program_details.program_name,'AnnualDay')
        self.assertEqual(program_details.student_count, 2)
        self.assertEqual(program_details.program_message, 'hello')


# Functional TestCases
class ProgramTest(TestCase):
    def setUp(self):
        self.dummy=ProgramInfo.program_info_save(program_name='happyholi',
                                              program_message='hi all',selected_ids=['1'])


    def test_program_info_method(self):

        resp=ProgramInfo.program_info_save(program_name='koushik', selected_ids=[1],program_message='hi all')
        response_data=resp

        with self.assertRaises(AssertionError):
            self.assertEqual(response_data.program_name,self.dummy.program_name)
        self.assertEqual(self.dummy.program_message,response_data.program_message)


class CampaignDetailsTest(TestCase):
    def setUp(self):
        location_instance = Location.objects.create(region='missouri')

        student_instance = StudentDetails.objects.create(student_name='koushik', student_location=location_instance,
                                                   masked_number='0998967878')

        phone_instance=PhoneNumber.objects.create(student_info=student_instance,mobile_number='0998967801')

        program_instance=ProgramInfo.program_info_save(program_name='koushik', selected_ids=[1], program_message='hi all')
        self.dummy=CampaignDetails.save_campaign_details(campaign=program_instance,list_numbers=[1])

    def test_save_campaign_details(self):

        resp=CampaignDetails.save_campaign_details(self.dummy[0].campaign,['1'])
        self.assertEqual(resp[0].campaign,self.dummy[0].campaign)
        self.assertEqual(resp[0].masked_number,self.dummy[0].masked_number)
        record=self.dummy[0].campaign.Phonenumbers_set.all()
        self.assertTrue(record.exist())

    def test_get_campaign_details(self):

        resp=CampaignDetails.campaign_details()
        self.assertTrue(resp.exists())
        self.assertEqual(resp.count(),2)


#Form Testing

class CampaignFormTest(TestCase):
    def test_campaign_form(self):
        fdata={'program_name':'Koushik','student_count':2,
                                   'selectedIds':['1','3'],'program_message':'hello'}

        form=ProgramInfoForm(data=fdata)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['program_name'],'Koushik')
        self.assertEqual(form.cleaned_data['student_count'], 2)
        self.assertIsNone(form.cleaned_data['program_document'],'')
        self.assertEqual(form.cleaned_data['program_message'], 'hello')

        #Negative TestCases

        self.assertNotEqual(form.cleaned_data['program_name'], 'SaiKoushik')
        self.assertNotEqual(form.cleaned_data['student_count'], 3)
        self.assertIsNotNone(form.cleaned_data['program_document'])
        self.assertNotEqual(form.cleaned_data['program_message'], 'helloworld')


