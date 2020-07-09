from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name = django-relative-softdeletion
  version = 0.1
  description = A Django models extension to add soft deletion functionality
  long_description=long_description,
  url = https://www.designstring.com/
  author = Designstring
  author_email = admin@designstring.com
  license = MIT
  classifiers = [
    Environment :: Web Environment
    Framework :: Django
    Framework :: Django :: X.Y  # Replace "X.Y" as appropriate
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Topic :: Internet :: WWW/HTTP
    Topic :: Internet :: WWW/HTTP :: Dynamic Content
  ]

)
