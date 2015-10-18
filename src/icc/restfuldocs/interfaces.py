from zope.interface import Interface, Attribute

class IConfiguration(Interface):
    CONFIGURATION = Attribute("Referance to a global configuration object.")