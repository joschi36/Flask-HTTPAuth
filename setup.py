"""
Flask-HTTPAuth
--------------

Basic and Digest HTTP authentication for Flask routes.
"""
from setuptools import setup


setup(
    name='JFlask-HTTPAuth',
    version='4.0.1',
    url='http://github.com/joschi36/flask-httpauth/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description='Basic and Digest HTTP authentication for Flask routes',
    long_description=__doc__,
    py_modules=['jflask_httpauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    test_suite="tests",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
