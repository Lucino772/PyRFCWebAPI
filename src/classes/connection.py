import uuid

try:
    from pyrfc import Connection
except:
    from .dummy import DummyPyRFCConnection as Connection

class ConnectionWrapper:

    def __init__(self, alias=None, client=None, user=None, passwd=None, lang=None, trace=None, ashost=None, sysnr=None, mshost=None, msserv=None, sysid=None, group=None, snc_qop=None, snc_myname=None, snc_partnername=None):
        self.conn_info = {
            'client': client,
            'user': user,
            'passwd': passwd,
            'lang': lang,
            'trace': trace,
            'ashost': ashost,
            'sysnr': sysnr,
            'mshost': mshost,
            'msserv': msserv,
            'sysid': sysid,
            'group': group,
            'snc_qop': snc_qop,
            'snc_myname': snc_myname,
            'snc_partnername': snc_partnername
        }
        self.alias = alias
        self.conn = Connection(**self.conn_info)
        self.id = uuid.uuid4().hex 

    @property
    def info(self):
        return dict(alias=self.alias, id=self.id, **self.conn_info)
