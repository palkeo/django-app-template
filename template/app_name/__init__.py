from django.conf import settings

app_settings = dict({
    'setting_name': 'value',
    }, **getattr(settings, "{{ app_name|upper }}_CONFIG", {}))

__version__ = '0.1'
