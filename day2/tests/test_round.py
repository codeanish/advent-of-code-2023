from day2.round import Round, build_round

def test_validate_round():
    assert Round(4,4,4).is_round_valid() == True
    assert Round(14,4,4).is_round_valid() == False
    assert Round(12,13,14).is_round_valid() == True

def test_build_round():
    first_round = build_round("3 blue, 4 red")
    assert first_round.red == 4
    assert first_round.blue == 3
    assert first_round.green == 0
    
    second_round = build_round("6 blue")
    assert second_round.red == 0
    assert second_round.blue == 6
    assert second_round.green == 0

    third_round = build_round("3 green, 15 blue, 14 red")
    assert third_round.red == 14
    assert third_round.blue == 15
    assert third_round.green == 3