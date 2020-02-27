from setuptools import setup

setup(
   name='event_registration',
   version='1.0',
   packages=['event_registration'],  #same as name
   install_requires=['django', 'djongo'], #external packages as dependencies
)