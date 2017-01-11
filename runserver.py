"""
This script runs the AzureFlask application using a development server.
"""

from os import environ
from AzureFlask import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '55225'))
    except ValueError:
        PORT = 55225
    app.run(HOST, PORT)
