from setuptools import setup

setup(
   name='mysite',
   version='0.0.1',
   author='Max MacCamy, Gabriel Meringolo',
   packages=['mysite'],
   license='LICENSE.txt',
   description='Django based web application that helps determine seasonality of produce based on location',
   long_description=open('README.md').read(),
   install_requires=[
       "Django >= 1.9.5",
       "django-extensions >= 1.6.7",
       "requests >= 2.9.1",
       "zipcode >= 2.0.0",
       "Sphinx >= 1.4.1",
   ],
)
