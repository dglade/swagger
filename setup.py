#!/usr/bin/env python

from distutils.core import setup

setup(name='SwaggerApp',
      version='1.0',
      description='Test app using swagger API documentation',
      author='Dan Glade',
      packages=['swagger_app', 'swagger_app.swagger_app'],
      data_files=[('.', ['requirements.txt', 'README.md',]),]
)
