# A Remarkbox theme is a python package with the following paths:
# 
#   template/<theme_name>-base.j2
#   static/theme/<theme_name>
#
# The theme needs to be registered to the 'remarkbox.themes'
# entry_point group to make it loaded by the Remarkbox application.

from setuptools import setup, find_packages

setup(name='remarkbox_westworld',
      version='0.2.0',
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
      keywords='remarkbox westworld theme',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points = {
        'remarkbox.themes' : [
            'westworld = remarkbox_westworld'
        ],
      },
)

