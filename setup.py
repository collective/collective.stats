import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.7'


setup(name='enfold.stats',
      version=version,
      description="Zope low level stats per request.",
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      author='Enfold Systems',
      author_email='contact@enfoldsystems.com',
      maintainer='Alex Clark',
      maintainer_email='aclark@aclark.net',
      url='http://www.enfoldsystems.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['enfold'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'ZODB3',
          'Zope2',
          'psutil',
      ],
      extras_require = dict(
        oldzope=['ZPublisherEventsBackport']),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      
      [console_scripts]
      es-parse = enfold.stats.export:main
      """,
      )
