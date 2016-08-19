import os

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings

from edc_label.apps import AppConfig as EdcLabelAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = '10.113.201.38'
    default_printer_label = 'leslie_testing'
    extra_templates_folder = os.path.join(settings.BASE_DIR, 'example', 'static', 'example')
