from setuptools import setup, find_packages

setup(
    name='RESTfulStorage',
    version='0.0.1',
    long_description=__doc__,
    packages=['RESTful-Storage'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-HTTPAuth',
        'Flask-RESTful',
    ]
)
