from django.apps import AppConfig as DjangoAppConfig

from edc_label.apps import AppConfig as EdcLabelAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    # default_cups_server_ip = '10.113.201.150'
    default_printer_label = '_10_113_200_59'
