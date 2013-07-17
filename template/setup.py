from distutils.core import setup
import os.path

from django.conf import settings
settings.configure()

import {{ app_name }}

PKG_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PKG_DIR, 'README.rst'), 'r') as f:
    long_description = f.read()

version = {{ app_name }}.__version__

setup(
    name = '{{ app_name }}',
    packages = ['{{ app_name }}'],
    version = version,
    description = '{{ short_description|default:"<SHORT_DESCRIPTION>" }}',
    long_description = long_description,
    author = '{{ author_name|default:"<AUTHOR_NAME>" }}',
    author_email = '{{ author_email|default:"<AUTHOR_EMAIL>" }}',
    url = 'https://github.com/{{ author_slug|default:"<AUTHOR>" }}/{{ app_name }}',
    download_url = 'https://github.com/{{ author_slug|default:"<AUTHOR>" }}/{{ app_name }}/tarball/%s' % version,
    keywords = ['{{ app_name }}'],
    classifiers = [
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    license='{{ license|default:"<LICENSE>" }}',
    requires=['Django (>= 1.4)']
)
