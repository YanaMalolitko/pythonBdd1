import os

from behave import given, then, when, step
import requests
import json

THIS_DIR = os.path.dirname(__file__)

@given(u'All pet store credentials are defined')
def step_impl(context):
    context.url = "http://petstore.swagger.io/v2/pet"
    context.headers = {'content-type': 'application/json'}
    context.body = {
        "id": 9876,
        "category": {
            "id": 9876,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 9876,
                "name": "string"
            }
        ],
        "status": "available"
    }


@when(u'I add the pet profile information with "{id}" to the "{website}"')
def step_impl(context, id, website):
    context.response = requests.put(website, data=json.dumps(context.body), headers=context.headers)


@step(u'Receive status code response {status}')
def step_impl(context, status):
    assert format(context.response.status_code) == format(status)


@then(u'I request the pet by {id}')
def step_impl(context, id):
    context.response = requests.get(context.url + id).decode('utf-8').replace('\0', '')


@step(u'Receive data format is proper')
def step_impl(context):
    print("Actual result:", json.dumps(context.response.json(), indent=4))
    my_data_path = os.path.join(THIS_DIR, 'testData.json')
    print("Expected result", my_data_path )

  #  assert json.dumps(context.response.json(), indent=4) == EXPECTED_JSON


@when(u'I remove the pet profile information with "{id}" from the "{website}"')
def step_impl(context, id, website):
    context.response = requests.delete(website + id)
