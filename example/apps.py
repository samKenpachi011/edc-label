import os

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings

from edc_label.apps import AppConfig as EdcLabelAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = None  # '10.113.200.252'  # '10.113.201.38'
    default_printer_label = 'Photosmart_C4500_series__AD3629_'
    extra_templates_folder = os.path.join(settings.BASE_DIR, 'example', 'static', 'example')
