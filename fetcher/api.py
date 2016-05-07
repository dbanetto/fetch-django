from django.conf import settings

import requests
import json
import logging

logger = logging.getLogger('fetch.api')
logger.debug("Fetcher url: {}".format(settings.FETCHER_URL))


def status():
    result = {"success": False}
    try:
        re = requests.get(settings.FETCHER_URL + '/status/')
        result = json.loads(re.content.decode('UTF-8'))
        result['success'] = True
    except Exception as e:
        logger.error('status: {}'.format(str(e)))
    return result


def force_fetch():
    try:
        re = requests.post(settings.FETCHER_URL + '/force/fetch/')
        result = json.loads(re.content.decode('UTF-8'))
    except Exception as e:
        logger.error('force_fetch: {}'.format(str(e)))
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
        logger.error('force_sort: {}'.format(str(e)))
        result = {
            'success': False,
            'error': '{}'.format(str(e))
        }
    return result
