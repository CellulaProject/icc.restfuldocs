from configure import CONFIG
from zope.configuration.xmlconfig import xmlconfig
from pkg_resources import resource_stream, resource_string
from icc.restfuldocs.interfaces import IConfiguration,IApplication
from zope.interface import implementer
from zope.component import getGlobalSiteManager, getUtility

from pyramid.config import Configurator
from waitress import serve
import icc.restfuldocs.views as docs_view
from pyramid.response import Response

package=__name__

@implementer(IConfiguration)
class Config(object):
    pass

conf=Config()

GSM=getGlobalSiteManager()

GSM.registerUtility(conf, IConfiguration, name='application')
conf.CONFIG=CONFIG
conf.CONFIG['GSM']=GSM

xmlconfig(resource_stream(package, "configure.zcml"))

def hello_world(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')

def application(global_config=None, **settings):
    config=Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    config.include(docs_view)
    app=config.make_wsgi_app()
    GSM.registerUtility(app, IApplication, name='application')
    return app

if __name__=="__main__":
    app=application()
    serve(app, host='::', port=6543)
    quit()
