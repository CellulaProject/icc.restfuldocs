from setuptools import setup, find_packages

setup(
    name='RESTfulStorage',
    version='0.0.1',
    long_description=__doc__,
    packages=['src'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-httpauth',
        'flask-restful',
    ]
)
quit()
