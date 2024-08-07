from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class UUIDMixin(models.Model):
    person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_contacted = models.DateTimeField(auto_now=True, verbose_name=_('Date of last contact'))

    class Meta:
        abstract = True

class Person(UUIDMixin, TimeStampedMixin):

    LEAD_SOURCE_CHOICES = [
        ('Internet Search', _('Internet Search')),
        ('Social Media', _('Social Media')),
        ('Blogs', _('Blogs')),
        ('Private Reccomendation', _('Private Reccomendation')),
        ('Podcasts', _('Podcasts')),
    ]

    LEAD_STATUS_CHOICES = [
        ('Not_processed', _('Not_processed')),
        ('In_progress', _('In_progress')),
        ('Processed', _('Processed')),
        ('Closed', _('Closed')),
    ]

    LEAD_CONTACT_PURPOSE = [
        ('IT_Infrastructure_Optimization', _('IT Infrastructure Optimization')),
        ('Information_Security', _('Information Security')),
        ('Project_Management', _('Project Management')),
        ('Web_Application_Development', _('Web Application Development')),
        ('Business_Process_Automation', _('Business Process Automation')),
        ('Marketing', _('Marketing')),
        ('Finance Analysis', _('Finance Analysis')),
        ('Data_Analysis', _('Data Analysis')),
        ('AI_Implementation', _('AI Implementation')),
        ('Efficiency_Improvement', _('Efficiency Improvement')),
        ('Post_Project_Support', _('Post-Project Support')),
        ('Business_Consulting', _('Business Consulting')),
        ('Mobile_App_Development', _('Mobile App Development')),
        ('CRM_Implementation', _('CRM Implementation')),
        ('API_Implementation', _('API Implementation')),
    ]

    # Контактная информация 

    first_name = models.CharField(verbose_name=_('Name'), null=True, blank=True, max_length=255)
    last_name = models.CharField(verbose_name=_('Surname'), null=True, blank=True, max_length=255)
    email = models.CharField(verbose_name=_('Email'), null=True, blank=True, max_length=255)
    phone_number = models.CharField(verbose_name=_('Phone Number'), null=True, blank=True, max_length=255)

    # Основная информация

    company = models.CharField(verbose_name=_('Company'), null=True, blank=True, max_length=255)
    position = models.CharField(verbose_name=_('Position'), null=True, blank=True, max_length=255)
    company_adress = models.CharField(verbose_name=_("Company's adress"), null=True, blank=True, max_length=255)

    # Информация о взаимодействии

    lead_status = models.CharField(choices=LEAD_STATUS_CHOICES, verbose_name=_('Lead Status'), null=True, blank=True, max_length=255)
    lead_source = models.CharField(choices=LEAD_SOURCE_CHOICES, verbose_name=_('Lead Source'), null=True, blank=True, max_length=255)
    exact_source = models.CharField(verbose_name=_('Exact Source'), null=True, blank=True, max_length=255)
    form_filling_page = models.CharField(verbose_name=_('Form filling page'), null=True, blank=True, max_length=255)
    total_visit_time = models.CharField(verbose_name=_('Total site visit time'), null=True, blank=True, max_length=255)

    # Интересы и потребности

    contact_purpose = models.CharField(choices=LEAD_CONTACT_PURPOSE, verbose_name=_('Lead Source'), null=True, blank=True, max_length=255)
    full_problem = models.CharField(verbose_name=_('Full problem'), null=True, blank=True, max_length=1025)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
    
    def __str__(self):
        return f"{self.name} | {self.email} | {self.lead_status}"