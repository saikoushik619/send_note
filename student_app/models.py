from operator import truediv

from django.db import models

# Create your models here.
class Location(models.Model):
    region = models.CharField(max_length=40)
    def __str__(self):
        return  f"{self.region}"

class StudentDetails(models.Model):
    student_name = models.CharField(max_length=40)
    student_location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    masked_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.student_name,self.student_location,self.masked_number)


    @classmethod
    def fetch_student_details(cls):
        return cls.objects.all().values('id','student_name','student_location__region','masked_number')
    @classmethod
    def fetch_single_region_students(cls,student_location):
        return cls.objects.filter(student_location__region__exact=student_location).values(
            'id','student_name','student_location__region','masked_number'
        )


class PhoneNumber(models.Model):
    student_info = models.ForeignKey(StudentDetails,on_delete=models.SET_NULL,null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.mobile_number


class ProgramInfo(models.Model):

    program_name=models.CharField(max_length=20)
    student_count=models.IntegerField()
    program_message=models.CharField(max_length=210)
    program_document=models.FileField(null=True,upload_to='student_updates/media',blank=True)
    program_date_time=models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,default='ready')

    def __str__(self):
        return self.program_name

    @classmethod
    def program_info_save(cls,program_name,selected_ids,program_message,program_document=None):
        student_count = len(selected_ids)
        if student_count < 1:
            raise Exception("required phone numbers.")

        save_program_info=cls.objects.create(program_name=program_name,
                                                     student_count=student_count,
                                                     program_message=program_message,
                                                     program_document=program_document)

        CampaignDetails.save_campaign_details(save_program_info, selected_ids)

        return save_program_info



    @classmethod
    def program_info_display(cls):
        return cls.objects.all().values('program_name',
                                        'student_count',
                                        'selected_ids',
                                        'program_message',
                                        'program_document')

class CampaignDetails(models.Model):
    campaign=models.ForeignKey(ProgramInfo,on_delete=models.SET_NULL,null=True)
    masked_number=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='ready')
    delivery_time=models.TimeField(null=True)

    def __str__(self):
        return self.masked_number

    @classmethod
    def save_campaign_details(cls, campaign, list_numbers):
        list_mobile_numbers = PhoneNumber.objects.filter(student_info_id__in=list_numbers).values(
            "mobile_number", "student_info__masked_number")

        rows = [cls(
            campaign=campaign,
            masked_number=num["student_info__masked_number"],
            phone_number=num["mobile_number"]
        ) for num in list_mobile_numbers]

        rows_ins = cls.objects.bulk_create(rows)

        return rows_ins

    @classmethod
    def campaign_details(cls):
        return cls.objects.all().values('masked_number','delivery_time','status')
