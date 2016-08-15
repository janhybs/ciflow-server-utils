from flask import Flask, render_template, url_for
from jinja2 import Template
from subprocess import check_output
from docker import docker

import os
import sys
import re
import time
import json

import humanfriendly

app = Flask(__name__)

package_regex = re.compile(r'([A-Z]+)_([0-9\.]+)_([a-z]+)', re.I)
extensions = ('.zip', '.tar.gz', '.deb')

def get_ext(f):
    for e in extensions:
        if f.endswith(e):
            return e
    return f.split('.')[-1]

def get_build_type_class(build_type):
    types = dict(
        debug="primary",
        release="success",
        dev="danger",
        )
    return types.get(build_type, 'default')

def split_path(path):
    folders = []
    while 1:
        path, folder = os.path.split(path)
        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break
    folders.reverse()
    return folders

def get_folders(cd='static/packages'):
    dirs = os.listdir(cd)
    dirs = [d for d in dirs if os.path.isdir(os.path.join(cd, d))]
    # dirs = [os.path.join(cd, d) for d in os.listdir(cd) if os.path.isdir(os.path.join(cd, d))]
    files = dict()
    for d in dirs:
        info = package_regex.match(d)
        if not info: continue

        name, version, build = info.groups()
        key = '{name}_{version}'.format(**locals())

        if not files.has_key(key):
            files[key] = dict()

        if not files[key].has_key(build):
            files[key][build] = dict()


        files[key][build]['files'] = list()
        package_files = [os.path.join(cd, d, f) for f in os.listdir(os.path.join(cd, d))]
        for f in package_files:
            item = dict()
            item['filename'] = f
            item['url'] = '/'.join(split_path(f)[1:])
            item['ext'] = get_ext(f)
            item['big'] = os.stat(f).st_size
            item['big_str'] = humanfriendly.format_size(item['big'])

            item['old'] = time.time() - os.path.getctime(f)
            item['old_str'] = ' '.join(humanfriendly.format_timespan(item['old']).split(' ')[0:2]).strip(',')
            files[key][build]['files'].append(item)
            files[key][build]['old_str'] = item['old_str']

    return files


def get_container_by_image(containers, image_name):
    for container in containers:
        if container['info']['image'] == image_name:
            return container
    return False

def parse_port(container):
    if not container:
        return []
    ports = container['info']['ports']
    result = []
    for port, binds in ports.items():
        port = port.strip('/tcpudp')
        
        if not binds:
            continue
            
        for bind in binds:
            if not bind or not bind.get('HostPort', False):
                continue
            result.append(dict(
                host=bind.get('HostPort'),
                cont=port
            ))
    return result
        

@app.route("/packages/")
def packages():
    return render_template(
        'packages.html', files=get_folders(),
        len=len, get_build_type_class=get_build_type_class
    )

@app.route("/")
def index():
    images = {
        'hybs/docker_jenkins:libs': {
            'class': 'jd',
            'name': 'Libs Jenkins',
            'port': '8081',
            'services': {
                'jenkins': 'service jenkins status',
                'docker': 'docker ps',
            }
        },
        'hybs/docker_jenkins:latest': {
            'class': 'jd',
            'name': 'Flow123d jenkins',
            'port': '8080',
            'services': {
                'jenkins': 'service jenkins status',
                'docker': 'docker ps',
            }
        },
    }
    containers = docker.get_docker_tree()
    view = dict()
    for i, v in images.items():
        view[i] = v.copy()
        container = get_container_by_image(containers, i)
        view[i]['status'] = bool(container)
        view[i]['ports'] = parse_port(container)
        
        if container:
            for name, command in view[i]['services'].items():
                cmd =  docker.get_command_prefix(path=[container['id']]) + ' ' + command
                try:
                    print check_output(cmd.split())
                    view[i]['services'][name] = True
                except:
                    view[i]['services'][name] = False
                    

    
    return render_template('index.html', view=view, len=len)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    app.run(host='0.0.0.0', port=80, debug=False)
    
    # print json.dumps(docker.get_docker_tree(), indent=4)
    # 
    # print json.dumps(get_folders(), indent=4)
    # print os.listdir('static/packages')
    
    #print docker.get_docker_tree()

    #exit(0)
