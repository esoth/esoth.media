# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

version = '1.0'

tests_require=['zope.testing']

setup(name='esoth.media',
      version=version,
      description="CDs, DVDs, etc. info",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python'
        ],
      keywords='',
      author='Esoth',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://github.com/esoth/esoth.media',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['esoth', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'esoth.media.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

