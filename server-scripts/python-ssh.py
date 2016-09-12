#!/bin/python
#

import os, sys
import getpass

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
profile_snippet = r"""
_sshh() {
    local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -W "ciflow tgh hybs hydra ci2runner paja tarkil meta skfm" -- $cur) )
}
complete -F _sshh sshh
"""

lookup = {
    "ciflow.nti.tul.cz": dict(
        user="root",
        tags="docker",
    ),
    "tgh.nti.tul.cz": dict(
        user="root",
    ),
    "ci2runner.nti.tul.cz": dict(
        user="root",
    ),
    "hybs.nti.tul.cz": dict(
        user="jan-hybs",
        port=8064,
    ),
    "hydra.kai.tul.cz": dict(
        user="jan.hybs",
    ),
    # "ci2runner.nti.tul.cz": dict(
    #     user="jan.hybs",
    # ),
    "paja.nti.tul.cz": dict(
        user="hybs",
        tags="skfm",
    ),
    "tarkil.cesnet.cz": dict(
        user="jan-hybs",
        tags="meta",
    ),
}

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

args = sys.argv[1:]
if len(sys.argv) < 2:
    import json, yaml
    print 'Registred entries:'
    print ''
    for url, v in lookup.items():
        vargs = ('\n       ').join(yaml.dump(v, default_flow_style=False).splitlines())
        print ' - {url}'.format(**locals())
        print '       {}'.format(vargs)
        print ''
    exit(1)


server = args[0]
user = args[1] if len(args) >= 2 else None
if user == '.':
    user = getpass.getuser()
verbose = '-v' if len(args) >= 3 else ''

def matches(url, value, server):
    if url.find(server) != -1:
        return True
        
    if value.get('tags', '').find(server) != -1:
        return True
    
    return False

for url, v in lookup.items():
    if matches(url, v, server):
        user = v.get('user', getpass.getuser()) if user is None else user
        port = int(v.get('port', 22))
        port_str = '' if port == 22 else '-p {port}'.format(**locals())
        
        command = "ssh {verbose} {port_str} {user}@{url}".format(**locals())
        print command
        exit(0)

print "No matching entry found for server {server}".format(**locals())
exit(1)