from zope.interface import Interface, Attribute

class IConfiguration(Interface):
    CONFIG = Attribute("Referance to a global configuration object.")

class IApplication(Interface):
    """The interface denotes application,
    used to mark an application object.
    """
