from subprocess import check_output
import json

def get_command_prefix(path=[]):
    command = []
    for i in path:
        command.extend(['docker', 'exec', i])
    return ' '.join(command)

def get_docker_tree(path=[]):
    command = get_command_prefix(path) + 'docker ps -q'

    try:
        ids = check_output(command.split()).strip()
    except:
        ids =''

    if not ids:
        return []

    ids = ids.split()
    result = []
    for cid in ids:
        container = dict()
        container['id'] = cid
        container['ids'] = get_docker_tree(path + [cid])

        info = dict()
        info['image'] = inspect_container(cid, path).get('Config', {}).get('Image', '')
        info['ports'] = inspect_container(cid, path).get('NetworkSettings', {}).get('Ports', [])
        info['volumes'] = inspect_container(cid, path).get('Mounts', [])
        container['info'] = info

        result.append(container)
    return result


def inspect_container(cid, path=[]):
    command = get_command_prefix(path) + 'docker inspect ' + str(cid)
    try:
        output = check_output(command.split())
        return json.loads(output)[0]
    except Exception as e:
        print e
        return {}
