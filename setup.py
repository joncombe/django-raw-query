# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-raw-query',
    version='0.0.4',
    author=u'Jon Combe',
    author_email='me@joncombe.net',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    license='BSD licence, see LICENCE file',
    description='Simple raw database query helper for Django',
    long_description='View readme on github: https://github.com/joncombe/django-raw-query',
    url='https://github.com/joncombe/django-raw-query',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
