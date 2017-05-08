import os

import requests

from .. import core

_sso_tokens = {}

def init_plugin():
    return {
        'tasks': {
            'sso': {
                'token': token_task,
            }
        }
    }


def get_config(options, args):
    return core.extend(args.get('sso', {}), options)


def generate_token(options, args):
    global _sso_tokens

    creds = core.get_credential(options['credentials'], args)
    username = creds['username']

    if username in _sso_tokens:
        return _sso_tokens[username]
    else:
        data = {
            'realm': creds.get('domain', 'jomax'),
            'username': creds['username'],
            'password': creds['password']
        }
        r = requests.post(options['url'], data)
        if r.status_code == 201:
            token = _sso_tokens[username] = r.json()['data']
            return token
        else:
            raise Exception('Unable to create SSO token [status=%s, resp=%s]' % (r.status_code, r.text))


def token_task(task, args, env):
    generate_token(task, args)
