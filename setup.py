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
	'waitress==0.8.11dev0ipv6-1',
	'cornice==1.2.0.dev0',
        #'flask',
        #'flask-httpauth',
        #'flask-restful',
        'zope.component [zcml]',
        'icc.contentstorage==0.0.1',
        'pudb',  # for debugging
    ],

    dependency_links = [
        'https://github.com/eugeneai/waitress/archive/0.8.11dev0ipv6-1.zip#egg=waitress-0.8.11dev0ipv6-1',
        'https://github.com/mozilla-services/cornice/archive/master.zip#egg=cornice-1.2.0.dev0',
	'https://github.com/eugeneai/icc.contentstorage/archive/master.zip#egg=icc.contentstorage-0.0.1',	
	],
    entry_points="""\
    [paste.app_factory]
    main = icc.app:application
    """,
)
quit()
