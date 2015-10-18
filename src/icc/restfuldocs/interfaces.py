from zope.interface import Interface, Attribute

class IApplication(Interface):
    CONFIGURATION = Attribute("Referance to a global configuration object.")