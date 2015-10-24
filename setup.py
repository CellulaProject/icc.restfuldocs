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
	'pyramid==1.6a2',
	'waitress==0.8.11dev0ipv6-1',
	'cornice==1.2.0.dev0',
        #'flask',
        #'flask-httpauth',
        #'flask-restful',
        'zope.component [zcml]',
        'icc.contentstorage',
        # 'pudb',  # for debugging
        'pyramid_zcml',
    ],

    dependency_links = [
        'https://github.com/Pylons/pyramid/archive/1.6a2.zip#egg=pyramid-1.6a2',
        'https://github.com/eugeneai/waitress/archive/0.8.11dev0ipv6-1.zip#egg=waitress-0.8.11dev0ipv6-1',
        'https://github.com/mozilla-services/cornice/archive/master.zip#egg=cornice-1.2.0.dev0'
	],
    entry_points="""\
    [paste.app_factory]
    main = icc.app:application
    """,
)
quit()
