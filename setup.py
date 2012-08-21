from setuptools import setup, find_packages
import os

version = '2.0-rhaptos'

setup(name='Products.ZPsycopgDA',
      version=version,
      description="",
      long_description="",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Michele Comitini',
      author_email='mcm@initd.org',
      url='http://initd.org',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      tests_require = [
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

