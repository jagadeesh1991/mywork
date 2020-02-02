# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:03:00 2020

@author: jaramasa
"""

from flask import json
from flask import Response
from flask_cors import CORS
from flask_api import FlaskAPI
import os
import datetime
#import pwd
APP = FlaskAPI(__name__)
CORS(APP)
@APP.route("/getStatus", methods=['GET'])
def get_stats_full():
    response_dict = {}
    try:
        filenamepath='marvel.json'
        st = os.stat(filenamepath)
       # userinfo = pwd.getpwuid(st.ST_UID)
        
        response_dict.update({'Last Access Time': datetime.datetime.fromtimestamp(st.st_atime)})
        response_dict.update({'Last Modification Time': datetime.datetime.fromtimestamp(st.st_mtime)})
        response_dict.update({'Last Change Time': datetime.datetime.fromtimestamp(st.st_ctime)})
        response_dict.update({'Index Node': st.st_ino})
        response_dict.update({'Size': st.st_size})
        response_dict.update({'Access Rights': st.st_mode})
        #response_dict.update({'UserName': userinfo})
        response_dict.update({'UserID': st.st_uid})
        js_dump = json.dumps(response_dict)
        resp1 = Response(js_dump,status=200,
                        mimetype='application/json')
        
    except FileNotFoundError as err:
        response_dict = {'error': 'file not found in server'}
        js_dump = json.dumps(response_dict)
        resp1 = Response(js_dump,status=500,
                        mimetype='application/json')
    return resp1


if __name__ == '__main__':
    APP.run()