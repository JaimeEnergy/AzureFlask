"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import AzureFlask.views

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer


class MyHandler(FTPHandler): 

    def on_connect(self):
        print ("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        print ("LOGGED IN")

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        print("FILE SENT")

    def on_file_received(self, file):
        # do something when a file has been received
        print("RECEIVED")

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)


def ftp():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.', perm='elradfmwM')
    authorizer.add_anonymous(homedir='.')

    handler = MyHandler
    handler.authorizer = authorizer
    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

import threading
threading.Thread(target=ftp).start()