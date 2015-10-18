#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""


from configure import CONFIG
from zope.configuration.xmlconfig import xmlconfig
from pkg_resources import resource_stream, resource_string
from icc.restfuldocs.interfaces import IConfiguration
from icc.contentstorage.interfaces import IDocumentStorage
from zope.interface import implementer
from zope.component import getGlobalSiteManager, getUtility

package=__name__


from flask import Flask, jsonify, abort, make_response, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth


#config_file=resource_stream(package, "application.ini")

@implementer(IConfiguration)
class Config(object):
    pass

conf=Config()

GSM=getGlobalSiteManager()

app = Flask(package, static_url_path="")

GSM.registerUtility(conf, IConfiguration, name='application')
conf.CONFIG=CONFIG
conf.CONFIG['GSM']=GSM

#app.name=package
#app.info="Main application global registry."

xmlconfig(resource_stream(package, "configure.zcml"))

api = Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'user':
        return 'pass'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 401)

class TaskListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.storage=getUtility(IDocumentStorage, "documents")
        super(TaskListAPI, self).__init__()

    def post(self):
        """Append new document to the storage"""

        data=request.get_data()
        sha_id=self.storage.put(data)
        return {'id': sha_id}, 201

class TaskAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.storage=getUtility(IDocumentStorage, "documents")
        super(TaskAPI, self).__init__()

    def get(self, sha_id):
        if len(sha_id) != 64:
            abort(404)
        try:
            data=self.storage.get(sha_id)
        except KeyError as e:
            return {'id': sha_id, 'exception':'KeyError', 'value': str(e)}
        print (repr(data))
        response=make_response(data)
        response.headers['Content-Type'] = 'Content-Type:application/octet-stream'
        return response

    def delete(self, sha_id):
        if len(sha_id) != 64:
            abort(404)
        try:
            key=self.storage.remove(sha_id)
        except KeyError as e:
            return {'id': sha_id, 'exception':'KeyError', 'value': str(e)}
        return {'id': key, 'deleted':True}


api.add_resource(TaskListAPI, '/content/', endpoint='tasks')
api.add_resource(TaskAPI, '/content/<sha_id>', endpoint='task')

@app.route('/')
def get_tasks():
    return 'Hello world'

if __name__ == '__main__':
    pass

#    import pudb; pu.db
    app.run(debug=True, host="::")
