from flask import Blueprint, request, jsonify
from .classes.connection import ConnectionWrapper

api_routes = Blueprint('api',__name__)

connections = []

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
    conns = [conn for conn in connections if conn.id == id]
    if len(conns) > 0:
        conn = conns[0]
        conn.conn.close()
        connections.remove(conn)
        return conn.info
    else:
        return {}
