from icc.restfuldocs.interfaces import IConfiguration
from icc.contentstorage.interfaces import IDocumentStorage
from zope.interface import implementer
from zope.component import getGlobalSiteManager, getUtility
from cornice import Service

doc_list = Service(name='list', path='/content', description="List of documents API")
doc = Service(name='content', path='/content/{sha_id}', description="Document API")

def storage(name='documents'):
    """Returns thw pointer to the document storage
    backend component.
    """
    return getUtility(IDocumentStorage, name)

def app(name='application'):
    """Return current application.
    """
    return getUtility(IApplication, name)

@doc_list.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}


# @auth.get_password
# def get_password(username):
#     if username == 'user':
#         return 'pass'
#     return None


# @auth.error_handler
# def unauthorized():
#     # return 403 instead of 401 to prevent browsers from displaying the default
#     # auth dialog
#     return make_response(jsonify({'message': 'Unauthorized access'}), 401)

@doc_list.post()
def post_doc():
    """Append new document to the storage"""

    data=request.get_data()
    sha_id=storage().put(data)
    return {'id': sha_id}, 201

@doc.get()
def get(sha_id):
        if len(sha_id) != 64:
            abort(404)
        try:
            data=storage().get(sha_id)
        except KeyError as e:
            return {'id': sha_id, 'exception':'KeyError', 'value': str(e)}
        response=make_response(data)
        response.headers['Content-Type'] = 'Content-Type:application/octet-stream'
        return response

@doc.delete()
def delete(self, sha_id):
        if len(sha_id) != 64:
            abort(404)
        try:
            key=storage().remove(sha_id)
        except KeyError as e:
            return {'id': sha_id, 'exception':'KeyError', 'value': str(e)}
        return {'id': key, 'deleted':True}

def includeme(config):
    'Add routes'
    # config.scan(__name__)
    # config.add_route('index', '')
    # config.add_route('debug', 'debug')
    # config.add_route('pdb', 'pdb')
