import uuid

try:
    from pyrfc import Connection
except:
    from .dummy import DummyPyRFCConnection as Connection

class ConnectionWrapper:

    def __init__(self, alias=None, **conn_info):
        self.conn_info = conn_info
        self.alias = alias
        self.conn = Connection(**self.conn_info)
        self.id = uuid.uuid4().hex 

    @property
    def info(self):
        return dict(alias=self.alias, id=self.id, **self.conn_info)
