import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.1.0'


setup(
    name='collective.stats',
    version=version,
    description="Zope low level stats per request.",
    long_description=open('README.rst').read() +
    open(os.path.join('docs', 'HISTORY.txt')).read(),
    classifiers=[
        "Environment :: Console",
        "Framework :: Plone",
        'Framework :: Plone :: 5.2',
        'Framework :: Plone :: 6.0',
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 5 - Production/Stable',
    ],
    author='Enfold Systems',
    author_email='contact@enfoldsystems.com',
    maintainer='Alex Clark',
    maintainer_email='aclark@aclark.net',
    url='http://github.com/collective/collective.stats',
    license='ZPL',
    keywords='collective stats plone zope',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'ZODB3',
        'Zope2',
        'psutil',
    ],
    extras_require=dict(
        oldzope=['ZPublisherEventsBackport']),
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone

      [console_scripts]
      collective-stats = collective.stats.export:main
      """,
)
