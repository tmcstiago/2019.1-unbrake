'''
Tests for models of calibration app
'''

import pytest
from django.test import Client
from calibration.models import CalibrationVibration, CalibrationForce
from calibration.models import CalibrationRelations, CalibrationTemperature
from calibration.models import CalibrationCommand, CalibrationSpeed


# First argument are the parameters names
# Second is a tuple of params
# First argument of param is the first parameter name and so on
# id is like the name for the test case
# Is possible to test only one test case with: pytest [file] -k [id]
@pytest.mark.django_db
def test_calibration_vibration():
    '''
        This test save a CalibrationVibration object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''

    CalibrationVibration(
        acquisition_temp=6,
        conversion_factor=1.00,
        vibration_offset=1.00,
    ).save()

    CalibrationVibration(
        acquisition_temp=7,
        conversion_factor=2.00,
        vibration_offset=2.00,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={calibrationVibration(id: 1)'
        '{acquisitionTemp, conversionFactor, vibrationOffset}}')
    assert result.status_code == 200
    single_aux = result.json()['data']['calibrationVibration']
    single_calibration_vibration = single_aux

    client = None
    result = None

    client = Client()
    result = client.get(
        '/graphql?query={allCalibrationVibration'
        '{id, acquisitionTemp, conversionFactor, vibrationOffset}}')
    assert result.status_code == 200
    multiple_aux = result.json()['data']['allCalibrationVibration']
    multiple_calibration_vibration_0 = multiple_aux[0]
    multiple_calibration_vibration_1 = multiple_aux[1]

    assert multiple_calibration_vibration_0['id'] == '1'
    assert multiple_calibration_vibration_1['id'] == '2'
    assert single_calibration_vibration['acquisitionTemp'] == 6
    assert single_calibration_vibration['conversionFactor'] == 1.00
    assert single_calibration_vibration['vibrationOffset'] == 1.00


@pytest.mark.django_db
def test_calibration_force():
    '''
        This test save a CalibrationForce object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''

    CalibrationForce(
        acquisition_temp=3,
        conversion_factor=1.000,
        force_offset=1.000,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={calibrationForce(id: 1)'
        '{acquisitionTemp, conversionFactor, forceOffset}}'
    )
    assert result.status_code == 200
    single_calibration_force = result.json()['data']['calibrationForce']

    CalibrationForce(
        acquisition_temp=4,
        conversion_factor=2.000,
        force_offset=2.000,
    ).save()

    result = None
    client = None

    client = Client()
    result = client.get(
        '/graphql?query={allCalibrationForce'
        '{id, acquisitionTemp, conversionFactor, forceOffset}}'
    )
    assert result.status_code == 200
    multiple_aux = result.json()['data']['allCalibrationForce']
    multiple_calibration_force_0 = multiple_aux[0]
    multiple_calibration_force_1 = multiple_aux[1]

    assert multiple_calibration_force_0['id'] == '1'
    assert multiple_calibration_force_1['id'] == '2'
    assert single_calibration_force['acquisitionTemp'] == 3
    assert single_calibration_force['conversionFactor'] == 1.000
    assert single_calibration_force['forceOffset'] == 1.000


@pytest.mark.django_db
def test_calibration_speed():
    '''
        This test save a CalibrationSpeed object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''

    CalibrationSpeed(
        acquisition_chanel=5,
        tire_radius=0.291550,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={calibrationSpeed(id: 1)'
        '{acquisitionChanel, tireRadius}}')
    assert result.status_code == 200
    single_calibration_speed = result.json()['data']['calibrationSpeed']

    CalibrationSpeed(
        acquisition_chanel=6,
        tire_radius=0.291551,
    ).save()

    client = None
    result = None

    client = Client()
    result = client.get(
        '/graphql?query={allCalibrationSpeed'
        '{id, acquisitionChanel, tireRadius}}')
    assert result.status_code == 200
    multiple_aux = result.json()['data']['allCalibrationSpeed']
    multiple_calibration_speed_0 = multiple_aux[0]
    multiple_calibration_speed_1 = multiple_aux[1]

    assert multiple_calibration_speed_0['id'] == '1'
    assert multiple_calibration_speed_1['id'] == '2'
    assert single_calibration_speed['acquisitionChanel'] == 5
    assert single_calibration_speed['tireRadius'] == 0.291550


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("acquisition_chanel_0,acquisition_chanel_1,"
     "tire_radius_0, tire_radius_1"),
    (pytest.param(5, 10, 0.291550, 0.583, id='all_speed_test_1'),
     )
)
def test_all_calibration_speed(acquisition_chanel_0, acquisition_chanel_1,
                               tire_radius_0, tire_radius_1):
    '''
        This test save two CalibrationSpeed objects on db,
        require all the saved objects by graphql,
        and check if the requirement is equal the saveds objects
    '''

    CalibrationSpeed(
        acquisition_chanel=acquisition_chanel_0,
        tire_radius=tire_radius_0,
    ).save()

    CalibrationSpeed(
        acquisition_chanel=acquisition_chanel_1,
        tire_radius=tire_radius_1,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={allCalibrationSpeed'
        '{id, acquisitionChanel, tireRadius}}')
    assert result.status_code == 200
    print(result.json())
    calibration_speed0 = result.json()['data']['allCalibrationSpeed'][0]
    calibration_speed1 = result.json()['data']['allCalibrationSpeed'][1]

    assert calibration_speed0['acquisitionChanel'] == acquisition_chanel_0
    assert calibration_speed0['tireRadius'] == tire_radius_0

    assert calibration_speed1['acquisitionChanel'] == acquisition_chanel_1
    assert calibration_speed1['tireRadius'] == tire_radius_1


@pytest.mark.django_db
def test_calibration_relations():
    '''
        This test save a CalibrationRelations object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''

    CalibrationRelations(
        transversal_selection_width=175,
        heigth_width_relation=65,
        rim_diameter=14,
        sync_motor_rodation=1700,
        sheave_move_diameter=12,
        sheave_motor_diameter=30,
    ).save()

    CalibrationRelations(
        transversal_selection_width=176,
        heigth_width_relation=66,
        rim_diameter=15,
        sync_motor_rodation=1701,
        sheave_move_diameter=13,
        sheave_motor_diameter=31,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={calibrationRelations(id: 1)'
        '{id, transversalSelectionWidth,'
        'heigthWidthRelation, rimDiameter, syncMotorRodation,'
        'sheaveMoveDiameter, sheaveMotorDiameter}}')
    assert result.status_code == 200
    single_aux = result.json()['data']['calibrationRelations']
    single_calibration_relations = single_aux

    client = None
    result = None

    client = Client()
    result = client.get(
        '/graphql?query={allCalibrationRelations'
        '{id, transversalSelectionWidth,'
        'heigthWidthRelation, rimDiameter, syncMotorRodation,'
        'sheaveMoveDiameter, sheaveMotorDiameter}}')
    assert result.status_code == 200

    multiple_aux = result.json()['data']['allCalibrationRelations']
    multiple_calibration_relations_0 = multiple_aux[0]
    multiple_calibration_relations_1 = multiple_aux[1]

    assert multiple_calibration_relations_0['id'] == '1'
    assert multiple_calibration_relations_1['id'] == '2'
    assert single_calibration_relations['transversalSelectionWidth'] == 175
    assert single_calibration_relations['heigthWidthRelation'] == 65
    assert single_calibration_relations['rimDiameter'] == 14
    assert single_calibration_relations['syncMotorRodation'] == 1700
    assert single_calibration_relations['sheaveMoveDiameter'] == 12
    assert single_calibration_relations['sheaveMotorDiameter'] == 30


@pytest.mark.django_db
def test_calibration_temperature():
    '''
        This test save a CalibrationTemperature object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''

    CalibrationTemperature(
        acquisition_temp=1,
        conversion_factor=0.200,
        temperature_offset=-1.2500,
    ).save()

    CalibrationTemperature(
        acquisition_temp=2,
        conversion_factor=0.400,
        temperature_offset=-2.500,
    ).save()

    client = Client()
    result = client.get(
        '/graphql?query={calibrationTemperature(id: 1)'
        '{acquisitionTemp, conversionFactor, temperatureOffset}}'
    )
    assert result.status_code == 200
    single_aux = result.json()['data']['calibrationTemperature']
    single_calibration_temperature = single_aux

    client = None
    result = None

    client = Client()
    result = client.get(
        '/graphql?query={allCalibrationTemperature'
        '{id, acquisitionTemp, conversionFactor, temperatureOffset}}'
    )
    assert result.status_code == 200
    multiple_aux = result.json()['data']['allCalibrationTemperature']
    multiple_calibration_temperature_0 = multiple_aux[0]
    multiple_calibration_temperature_1 = multiple_aux[1]

    assert multiple_calibration_temperature_0['id'] == '1'
    assert multiple_calibration_temperature_1['id'] == '2'
    assert single_calibration_temperature['acquisitionTemp'] == 1
    assert single_calibration_temperature['conversionFactor'] == 0.200
    assert single_calibration_temperature['temperatureOffset'] == -1.2500


@pytest.mark.django_db
def test_calibration_commands():
    '''
        This test save a CalibrationCommand object on db,
        require the saved object by graphql,
        and check if the requirement is equal the saved object
    '''

    CalibrationCommand(
        command_chanel_speed=7,
        actual_speed=0.000,
        max_speed=100.000,
        chanel_command_pression=8,
        actual_pression=0.000,
        max_pression=30.000,
    ).save()

    CalibrationCommand(
        command_chanel_speed=6,
        actual_speed=1.000,
        max_speed=101.000,
        chanel_command_pression=9,
        actual_pression=1.000,
        max_pression=31.000,
    ).save()

    client = Client()
    result_single = client.get(
        '/graphql?query={calibrationCommand(id: 1)'
        '{commandChanelSpeed,actualSpeed,maxSpeed,'
        'chanelCommandPression,actualPression,maxPression}}')
    assert result_single.status_code == 200

    single_aux = result_single.json()['data']['calibrationCommand']
    single_calibration_commands = single_aux

    result_multiple = client.get(
        '/graphql?query={allCalibrationCommand'
        '{id,commandChanelSpeed,actualSpeed,maxSpeed,'
        'chanelCommandPression,actualPression,maxPression}}')
    assert result_multiple.status_code == 200

    multiple_aux = result_multiple.json()['data']['allCalibrationCommand']
    multiple_calibration_commands_0 = multiple_aux[0]
    multiple_calibration_commands_1 = multiple_aux[1]

    assert multiple_calibration_commands_0['id'] == '1'
    assert multiple_calibration_commands_1['id'] == '2'
    assert single_calibration_commands['commandChanelSpeed'] == 7
    assert single_calibration_commands['actualSpeed'] == 0.000
    assert single_calibration_commands['maxSpeed'] == 100.000
    assert single_calibration_commands['chanelCommandPression'] == 8
    assert single_calibration_commands['actualPression'] == 0.000
    assert single_calibration_commands['maxPression'] == 30.000
