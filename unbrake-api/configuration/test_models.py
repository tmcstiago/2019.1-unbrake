'''
Tests for models of configuration app
'''

import pytest
from django.test import Client
from configuration.models import Config


# First argument are the parameters names
# Second is a tuple of params
# First argument of param is the first parameter name and so on
# id is like the name for the test case
# Is possible to test only one test case with: pytest [file] -k [id]
@pytest.mark.django_db
@pytest.mark.parametrize(
    ("parameters"), (
        pytest.param([10, 20, 32, 16, 5, 5, True, False, 64, 51],
                     id='config_test_1'),
    )
)
def test_config(parameters):
    '''
        This test save a ConfigType object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''
    number_aux = parameters[0]
    time_between_cycles_aux = parameters[1]
    upper_limit_aux = parameters[2]
    inferior_limit_aux = parameters[3]
    upper_time_aux = parameters[4]
    inferior_time_aux = parameters[5]
    disable_shutdown_aux = parameters[6]
    enable_output_aux = parameters[7]
    temperature_aux = parameters[8]
    time_aux = parameters[9]

    Config(
        number=number_aux,
        time_between_cycles=time_between_cycles_aux,
        upper_limit=upper_limit_aux,
        inferior_limit=inferior_limit_aux,
        upper_time=upper_time_aux,
        inferior_time=inferior_time_aux,
        disable_shutdown=disable_shutdown_aux,
        enable_output=enable_output_aux,
        temperature=temperature_aux,
        time=time_aux,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={config(id: 1){number, timeBetweenCycles, upperLimit,'
        'inferiorLimit, upperTime, inferiorTime,'
        'disableShutdown, enableOutput, temperature,time}}')

    assert result.status_code == 200
    cycles_config = result.json()['data']['config']
    assert cycles_config['number'] == number_aux
    assert cycles_config['timeBetweenCycles'] == time_between_cycles_aux
    assert cycles_config['upperLimit'] == upper_limit_aux
    assert cycles_config['inferiorLimit'] == inferior_limit_aux
    assert cycles_config['upperTime'] == upper_time_aux
    assert cycles_config['inferiorTime'] == inferior_time_aux
    assert cycles_config['disableShutdown'] == disable_shutdown_aux
    assert cycles_config['enableOutput'] == enable_output_aux
    assert cycles_config['temperature'] == temperature_aux
    assert cycles_config['time'] == time_aux


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("parameters"), (
        pytest.param([10, 20, 32, 16, 5, 5, 'true', 'false', 64, 51],
                     id='create_config_test_1'),
    )
)
def test_create_config(parameters):
    '''
        This test create an object on db using a post request,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''
    number = parameters[0]
    time_between_cycles = parameters[1]
    upper_limit = parameters[2]
    inferior_limit = parameters[3]
    upper_time = parameters[4]
    inferior_time = parameters[5]
    disable_shutdown = parameters[6]
    enable_output = parameters[7]
    temperature = parameters[8]
    time = parameters[9]

    client = Client()
    create = client.post(
        '/graphql?query=mutation{createConfig'
        '(number: ' + str(number) + ', '
        'timeBetweenCycles: ' + str(time_between_cycles) + ', '
        'upperLimit: ' + str(upper_limit) + ', '
        'inferiorLimit: ' + str(inferior_limit) + ', '
        'upperTime: ' + str(upper_time) + ', '
        'inferiorTime: ' + str(inferior_time) + ', '
        'disableShutdown: ' + str(disable_shutdown) + ', '
        'enableOutput: ' + str(enable_output) + ', '
        'temperature: ' + str(temperature) + ', '
        'time: ' + str(time) + ')'
        '{config{number, timeBetweenCycles,upperLimit,inferiorLimit,'
        'upperTime, inferiorTime, disableShutdown,'
        'enableOutput, temperature, time}}}')
    assert create.status_code == 200

    result = client.get(
        '/graphql?query=query{config(id: 1){number, timeBetweenCycles,'
        ' upperLimit, inferiorLimit, upperTime, inferiorTime,'
        'disableShutdown, enableOutput, temperature,time}}')
    assert result.status_code == 200

    assert create.json()['data']['createConfig'] == result.json()['data']
