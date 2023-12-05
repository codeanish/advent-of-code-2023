
from day5.main import get_destination
from day5.mapping import Mapping


# def test_get_destination():
#     mappings = [Mapping(50,98,2), Mapping(52,50,48)]
#     assert get_destination(13, mappings) == 13
#     assert get_destination(55, mappings) == 57
#     assert get_destination(14, mappings) == 14
#     assert get_destination(79, mappings) == 81


def test_seed_to_soil():
    mappings = [Mapping(50,98,2), Mapping(52,50,48)]
    assert get_destination(13, mappings) == 13
    assert get_destination(55, mappings) == 57
    assert get_destination(14, mappings) == 14
    assert get_destination(79, mappings) == 81

def test_soil_to_fertilizer():
    mappings = [Mapping(0,15,37), Mapping(37,52,2), Mapping(39,0,15)]
    assert get_destination(81, mappings) == 81
    assert get_destination(14, mappings) == 53
    assert get_destination(57, mappings) == 57
    assert get_destination(13, mappings) == 52

def test_fertilizer_to_water():
    mappings = [Mapping(49,53,8), Mapping(0,11,42), Mapping(42,0,7), Mapping(57,7,4)]
    assert get_destination(81, mappings) == 81
    assert get_destination(53, mappings) == 49
    assert get_destination(57, mappings) == 53
    assert get_destination(52, mappings) == 41

def test_water_to_light():
    mappings = [Mapping(88,18,7), Mapping(18,25,70)]
    assert get_destination(81, mappings) == 74
    assert get_destination(49, mappings) == 42
    assert get_destination(53, mappings) == 46
    assert get_destination(41, mappings) == 34

def test_light_to_temperature():
    mappings = [Mapping(45,77,23), Mapping(81,45,19), Mapping(68,64,13)]
    assert get_destination(74, mappings) == 78
    assert get_destination(42, mappings) == 42
    assert get_destination(46, mappings) == 82
    assert get_destination(34, mappings) == 34

def test_temperature_to_humidity():
    mappings = [Mapping(0,69,1), Mapping(1,0,69)]
    assert get_destination(78, mappings) == 78
    assert get_destination(42, mappings) == 43
    assert get_destination(82, mappings) == 82
    assert get_destination(34, mappings) == 35

def test_humidity_to_location():
    mappings = [Mapping(60,56,37), Mapping(56,93,4)]
    assert get_destination(78, mappings) == 82
    assert get_destination(43, mappings) == 43
    assert get_destination(82, mappings) == 86
    assert get_destination(35, mappings) == 35