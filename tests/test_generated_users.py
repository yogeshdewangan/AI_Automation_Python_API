import requests
import pytest

import pytest
import requests
import json
import logging

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('test.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = get_logger()

def test_get_request():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        logger.info('GET request sent')
        print(response)
        assert response.status_code == 201, 'Status code is not 201'
        logger.info('Status code checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_json_key():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        data = response.json()
        assert 'id' in data, 'Key "id" not in response'
        logger.info('Key checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_json_value():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        data = response.json()
        assert data['id'] == 1, 'Value of "id" is not 1'
        logger.info('Value checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_type():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert isinstance(response, requests.models.Response), 'Response is not of type requests.models.Response'
        logger.info('Response type checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_headers():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert 'content-type' in response.headers, 'Header "content-type" not in response'
        logger.info('Header checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_time():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert response.elapsed.total_seconds() < 1, 'Response time is more than 1 second'
        logger.info('Response time checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_encoding():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert response.encoding == 'utf-8', 'Encoding is not utf-8'
        logger.info('Encoding checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_url():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert response.url == 'https://jsonplaceholder.typicode.com/users/1', 'URL is not correct'
        logger.info('URL checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_cookies():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert response.cookies == {}, 'Cookies are not empty'
        logger.info('Cookies checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))

def test_response_history():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert response.history == [], 'History is not empty'
        logger.info('History checked')
    except AssertionError as e:
        logger.error('Test failed: {}'.format(e))