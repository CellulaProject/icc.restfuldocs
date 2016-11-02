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
	'pyramid',
	'waitress',
	'cornice',
        'zope.component [zcml]',
        'icc.contentstorage==0.0.1',
        'pudb',  # for debugging
    ],

    dependency_links = [
	'https://github.com/eugeneai/icc.contentstorage/archive/master.zip#egg=icc.contentstorage-0.0.1',	
	],
    entry_points="""\
    [paste.app_factory]
    main = icc.app:application
    """,
)
quit()
