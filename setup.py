from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import ffman

here = os.path.abspath(os.path.dirname(__file__))

long_description = """
FFMPEG wrapper for Python.
Note that the platform-specific wheels contain the binary executable
of ffmpeg, which makes this package around 60 MiB in size.
I guess that's the cost for being able to read/write video files.
For Linux users: the above is not the case when installing via your
Linux package manager (if that is possible), because this package would
simply depend on ffmpeg in that case.
""".lstrip()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='ffman',
    version=ffman.__version__,
    url='https://github.com/leowenyang/ffman',
    license='Apache Software License',
    author='leowenyang',
    author_email='leowenyang@163.com',
    tests_require=['pytest'],
    install_requires=[
    ],
    cmdclass={'test': PyTest},
    description='Automated REST APIs for existing database-driven systems',
    long_description=long_description,
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_dir={"ffman": "ffman"},
    package_data={"ffman": ["data/dlib/*.dat", "data/haarcascades/*.xml"]},
    include_package_data=True,
    platforms='any',
    test_suite='ffman.tests.test_ffman',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: Chinese',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)