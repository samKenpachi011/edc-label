# from django.db import models
# 
# from edc_base.model.models.base_uuid_model import BaseUuidModel
# from edc_registration.models import RegisteredSubjectModelMixin, RegisteredSubjectManager
# 
# 
# class Aliquot(BaseUuidModel):
# 
#     aliquot_identifier = models.CharField(max_length=25)
# 
#     aliquot_type = models.CharField(max_length=25)
# 
#     class Meta:
#         app_label = 'example'
# 
# 
# class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):
# 
#     objects = RegisteredSubjectManager()
# 
#     class Meta:
#         app_label = 'example'
