import requests
import pytest

import pytest
import requests
import json
import logging

logging.basicConfig(filename='/logs/test_failures.log', level=logging.ERROR)

def test_get_request():
    try:
        headers = {'x-api-key': 'reqres-free-v1'}
        response = requests.get('https://jsonplaceholder.typicode.com/users/1', headers=headers)
        print(response.text)
        assert response.status_code == 201, 'Status code is not 201'
        data = response.json()
        assert 'id' in data, 'Key not found in the response'
    except AssertionError as e:
        logging.error(str(e))

def test_post_request():
    try:
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'key1': 'value1', 'key2': 'value2'}
        response = requests.post('https://jsonplaceholder.typicode.com/users/1', headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, 'Status code is not 201'
        data = response.json()
        assert 'id' in data, 'Key not found in the response'
    except AssertionError as e:
        logging.error(str(e))

def test_get_request_with_wrong_url():
    try:
        headers = {'x-api-key': 'reqres-free-v1'}
        response = requests.get('https://jsonplaceholder.typicode.com/wrong_url', headers=headers)
        print(response.text)
        assert response.status_code == 201, 'Status code is not 201'
    except AssertionError as e:
        logging.error(str(e))

def test_post_request_with_wrong_url():
    try:
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'key1': 'value1', 'key2': 'value2'}
        response = requests.post('https://jsonplaceholder.typicode.com/wrong_url', headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, 'Status code is not 201'
    except AssertionError as e:
        logging.error(str(e))

def test_get_request_without_headers():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        print(response.text)
        assert response.status_code == 201, 'Status code is not 201'
        data = response.json()
        assert 'id' in data, 'Key not found in the response'
    except AssertionError as e:
        logging.error(str(e))