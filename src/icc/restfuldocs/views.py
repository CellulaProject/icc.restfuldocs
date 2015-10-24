from icc.restfuldocs.interfaces import IConfiguration
from icc.contentstorage.interfaces import IDocumentStorage
from zope.interface import implementer
from zope.component import getGlobalSiteManager, getUtility
from cornice.resource import add_resource, add_view
from pyramid.response import Response
import cornice


def storage(name='documents'):
    """Returns thw pointer to the document storage
    backend component.
    """
    return getUtility(IDocumentStorage, name)

def app(name='application'):
    """Return current application.
    """
    return getUtility(IApplication, name)

def abort(status):
    return Response(status_code=status)

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


class Documents(object):
    """
    """

    def __init__(self, request):
        """
        """
        self.request=request

    def collection_post(self):
        """Append new document to the storage"""

        data=self.request.body
        print (type(data),self.request.content_length)
        sha_id=storage().put(data)
        return {'id': sha_id}

    def collection_get(self):
        return {'text':'Hello world!'}

    def get(self):
        sha_id=self.request.matchdict['id']
        if len(sha_id) != 64:
            abort(404)
        try:
            data=storage().get(sha_id)
        except KeyError as e:
            return {'id': sha_id, 'exception':'KeyError', 'value': str(e)}
        response=Response(
            content_type='application/octet-stream',
            body=data
        )
        return response

    def delete(self, sha_id):
        sha_id=self.request.matchdict['id']
        if len(sha_id) != 64:
            abort(404)
        try:
            key=storage().remove(sha_id)
        except KeyError as e:
            return {'id': sha_id, 'exception':'KeyError', 'value': str(e)}
        return {'id': key, 'deleted':True}

#add_view(Documents.collection_post, renderer='json', status=201)
#add_view(Documents.get, renderer='json')
#add_view(Documents.delete, renderer='json')

document_resource = add_resource(
    Documents,
    path='/content/{id}',
    collection_path='/content',
) #, description="Document API")

def includeme(config):
    config.add_cornice_resource(document_resource)
