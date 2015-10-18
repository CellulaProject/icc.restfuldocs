from setuptools import setup, find_packages

setup(
    name='icc.restfuldocs',
    version='0.0.1',
    long_description=__doc__,
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-httpauth',
        'flask-restful',
        'zope.component [zcml]',
        'icc.contentstorage',
        'pudb',  # for debugging
    ],
)
quit()
