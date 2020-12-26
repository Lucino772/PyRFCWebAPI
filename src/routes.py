from flask import Blueprint, request, jsonify
from .classes.connection import ConnectionWrapper
from .utils.read_table import readtable

api_routes = Blueprint('api',__name__)

connections = []

def get_connection_by_id(id):
    conns = [conn for conn in connections if conn.id == id]
    if len(conns) > 0:
        return conns[0]
    
    return None

## Connections ##
@api_routes.route('/connection',methods=['GET'])
def get_connections():
    global connections
    infos = [conn.info for conn in connections]
    return jsonify(infos)

@api_routes.route('/connection/<id>',methods=['GET'])
def get_connection(id):
    global connections
    infos = [conn.info for conn in connections if conn.id == id]
    if len(infos) > 0:
        return infos[0]
    else:
        return {}

@api_routes.route('/connection',methods=['POST'])
def create_connection():
    global connections
    info = request.get_json()
    conn = ConnectionWrapper(**info)
    connections.append(conn)
    return conn.info

@api_routes.route('/connection/<id>',methods=['DELETE'])
def delete_connection(id):
    global connections
    conn = get_connection_by_id(id)
    if conn:
        conn.conn.close()
        connections.remove(conn)
        return conn.info
    else:
        return {}

## Calls ##
@api_routes.route('/bapi/<id>/<bapi>',methods=['GET','POST'])
def bapi_call_or_description(id, bapi):
    conn = get_connection_by_id(id)
    if conn:
        if request.method == 'GET': # Get function description
            pass 
        else: # Call the BAPI
            data = request.get_json()
            result = conn.conn.call(bapi,**data)
            return jsonify(result)
    else:
        return {
            'error': f'Connection id ({id}) does not exists !'
        }

@api_routes.route('/table/<id>/<table>', methods=['GET'])
def read_table(id, table):
    conn = get_connection_by_id(id)
    if conn:
        data = request.json()
        result = readtable(conn.conn, table, data.get('fields',[]), data.get('options'))
        return jsonify(result)
    else:
        return {}
