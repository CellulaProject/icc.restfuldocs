from icc.storage.kcstorage.components import *
from icc.restfuldocs.interfaces import IApplication
from zope.component import getUtility

app=getUtility(IApplication, 'application')

CONFIG=app.CONFIG

storage=KiotoCabinetDocStorage(CONFIG['CONTENT_STORAGE_FILENAME'])
