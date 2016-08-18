from django.apps import AppConfig as DjangoAppConfig

from edc_label.apps import AppConfig as EdcLabelAppConfigParent
from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    # default_cups_server_ip = '10.113.201.150'
    default_printer_label = '_10_113_200_59'


class EdcRegistrationAppConfig(EdcRegistrationAppConfigParent):
    app_label = 'example'
