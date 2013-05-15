#coding=utf8

from flask import Flask, request
import json
import glob

import imp

app = Flask(__name__)
DEBUG = True



# define payload from github
class Commit:
    def __init__(self):
        self.id = ""
        self.message = ""
        

class PayLoad:
    def __init__(self, data):
        self.commits = []


@app.route("/")
def index():
    return fire()

@app.route("/fire", methods=["POST"])
def fire():
    # rawjson = request.form["payload"]
    # data = json.load(rawjson)
    # payload = PayLoad(data)
    
    files = find_scripts()
    for each_file in files:
        execute_script(each_file)

    return ""
    
def find_scripts(branch_name=None):
    return glob.glob('scripts/*.py')
    
    
def execute_script(script_name):
    module = imp.load_source('module', script_name)
    module.run()


if __name__ == "__main__":
    if DEBUG:
        app.run(host="0.0.0.0", port=1234, debug=True)
    else:
        import os
        os.system('gunicorn app:app')
    