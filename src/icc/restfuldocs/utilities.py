from icc.contentstorage.kyotocabinet.components import *
#from icc.contentstorage.dictionary.components import *
#from icc.contentstorage.kyototycoon.components import *
from icc.restfuldocs.interfaces import IConfiguration
from zope.component import getUtility

app=getUtility(IConfiguration, 'application')

CONFIG=app.CONFIG

storage=KiotoCabinetDocStorage(CONFIG['CONTENT_STORAGE_FILENAME'])
#storage=KiotoTycoonDocStorage()
#storage=DictionaryDocStorage()
