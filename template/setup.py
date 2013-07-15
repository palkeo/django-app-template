from distutils.core import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

with open('VERSION', 'r') as f:
    version = f.read().strip()

setup(
    name = '{{ app_name }}',
    packages = ['{{ app_name }}'],
    version = version,
    description = '{{ short_description }}',
    long_description = long_description,
    author = '{{ author_name }}',
    author_email = '{{ author_email }}',
    url = 'https://github.com/{{ author_slug }}/{{ app_name }}',
    download_url = 'https://github.com/{{ author_slug }}/{{ app_name }}/tarball/%s' % version,
    keywords = ['{{ app_name }}'],
    classifiers = [
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    license='{{ license }}',
    requires=['Django (>= 1.4)']
)
