from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name="django-relative-softdeletion",
  version= "0.0.2",
  description="A Django models extension to add soft deletion functionality",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/DesignString/django-relative-soft-deletion",
  author="Designstring",
  author_email="admin@designstring.com",
  license ="MIT",
  classifiers = [
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"
  ]

)
