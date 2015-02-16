# -*- coding: utf-8 -*-

"""
    Eve Demo on OpenShift
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.
    Running on OpenShift

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    Instructions on how to start your own instance on OpenShift can be found in the README.rst

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os
import sys
from eve import Eve

#eve-docs - not compatible with Python3
#from flask.ext.bootstrap import Bootstrap
#from eve_docs import eve_docs

''' OpenShift setup virtual environment - not required
PYCART_DIR = ''.join(['python-', '.'.join(map(str, sys.version_info[:2]))])

try:
   zvirtenv = os.path.join(os.environ.get('OPENSHIFT_HOMEDIR', '~'), PYCART_DIR,
                           'virtenv', 'bin', 'activate_this.py')
   exec(compile(open(zvirtenv).read(), zvirtenv, 'exec'),
        dict(__file__ = zvirtenv) )
except IOError:
   pass
'''

# OpenShift support: bind to OpenShift environment variables if available
host = os.environ.get('OPENSHIFT_PYTHON_IP', 'localhost')
port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', '5000'))


# use imp to import application?
app = Eve()


''' Deleted but not forgotten
@app.after_request
def after_request(response):
    response.headers.add('X-Ahmed', 'Je Suis Ahmed.')
    response.headers.add('X-Charlie', 'Je Suis Charlie.')
    return response
'''

if __name__ == '__main__':
#    Bootstrap(app)
#    app.register_blueprint(eve_docs, url_prefix='/docs')
    print('Starting API on http://' + host + ':' + str(port))
    app.run(host=host, port=port)
