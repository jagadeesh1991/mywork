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
#import pwd
APP = FlaskAPI(__name__)
CORS(APP)
@APP.route("/getFileLoc", methods=['GET'])
def get_File_Location():
    response_dict = {}
    try:
        filenamepath='marvel.json'
        st = os.stat(filenamepath)

        response_dict.update({'File Index Node': st.st_ino})
        response_dict.update({'File Device': st.st_dev})
        response_dict.update({'File Device Type': st.st_rdev})

        info = os.statvfs(filenamepath) 
        print(info)
        
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump,status=200,
                        mimetype='application/json')
        
    except FileNotFoundError as err:
        response_dict = {'error': 'file not found in server'}
        js_dump = json.dumps(response_dict)
        resp1 = Response(js_dump,status=500,
                        mimetype='application/json')
    return resp


if __name__ == '__main__':
    APP.run()