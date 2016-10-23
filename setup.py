import os

from setuptools import setup, find_packages

setup(name='remarkbox_westworld',
      version='0.0.1',
      description='remarkbox westworld theme',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Russell Ballestrini',
      author_email='russell@ballestrini.net',
      url='http://russell.ballestrini.net',
      keywords='remarkbox theme',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
)

