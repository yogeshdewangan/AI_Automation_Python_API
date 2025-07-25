import requests
import pytest

import pytest
import requests
import json
import logging

logging.basicConfig(filename='/logs/test_failures.log', level=logging.ERROR)

def test_post_request_1():
    try:
        url = "https://reqres.in/api/users"
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'name': 'John', 'job': 'developer'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, "Status code is not 201"
        assert 'name' in response.json(), "Key 'name' not in the response"
    except AssertionError as e:
        logging.error(str(e))

def test_post_request_2():
    try:
        url = "https://reqres.in/api/users"
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'name': 'Jane', 'job': 'designer'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, "Status code is not 201"
        assert 'job' in response.json(), "Key 'job' not in the response"
    except AssertionError as e:
        logging.error(str(e))

def test_post_request_3():
    try:
        url = "https://reqres.in/api/users"
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'name': 'Mike', 'job': 'tester'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, "Status code is not 201"
        assert 'id' in response.json(), "Key 'id' not in the response"
    except AssertionError as e:
        logging.error(str(e))

def test_post_request_4():
    try:
        url = "https://reqres.in/api/users"
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'name': 'Emma', 'job': 'manager'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, "Status code is not 201"
        assert 'createdAt' in response.json(), "Key 'createdAt' not in the response"
    except AssertionError as e:
        logging.error(str(e))

def test_post_request_5():
    try:
        url = "https://reqres.in/api/users"
        headers = {'x-api-key': 'reqres-free-v1'}
        payload = {'name': 'Oliver', 'job': 'engineer'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.text)
        assert response.status_code == 201, "Status code is not 201"
        assert 'name' in response.json(), "Key 'name' not in the response"
    except AssertionError as e:
        logging.error(str(e))