from django.conf import settings

import requests
import json


def status():
    try:
        re = requests.get(settings.FETCHER_URL + '/status/')
        content = re.content.decode('UTF-8')
        result = json.loads(content)
        result['success'] = True
    except Exception as e:
        result = {
            'success': False,
            'running': False,
            'content': content,
            'error': '{}'.format(str(e))
        }
    return result


def force_fetch():
    try:
        re = requests.post(settings.FETCHER_URL + '/force/fetch/')
        result = json.loads(re.content.decode('UTF-8'))
    except Exception as e:
        result = {
            'success': False,
            'error': '{}'.format(str(e))
        }
    return result


def force_sort():
    try:
        re = requests.post(settings.FETCHER_URL + '/force/sort/')
        result = json.loads(re.content.decode('UTF-8'))
    except Exception as e:
        result = {
            'success': False,
            'error': '{}'.format(str(e))
        }
    return result
