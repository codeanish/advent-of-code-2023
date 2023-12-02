
from day1.main import get_calibration_value


def test_get_calibration_value():
    assert get_calibration_value("1abc2") == 12
    assert get_calibration_value("pqr3stu8vwx") == 38
    assert get_calibration_value("a1b2c3d4e5f") == 15
    assert get_calibration_value("treb7uchet") == 77
    assert get_calibration_value("") == 0
    assert get_calibration_value("abc") == 0
    assert get_calibration_value("1xxxxxxxxxxxxxxxxxxxxxxx1") == 11
    assert get_calibration_value("172") == 12

def test_replace_text_numbers_with_digits():
    assert get_calibration_value("two1nine") == 29
    assert get_calibration_value("eightwothree") == 83
    assert get_calibration_value("abcone2threexyz") == 13
    assert get_calibration_value("xtwone3four") == 24
    assert get_calibration_value("4nineeightseven2") == 42
    assert get_calibration_value("zoneight234") == 14
    assert get_calibration_value("7pqrstsixteen") == 76