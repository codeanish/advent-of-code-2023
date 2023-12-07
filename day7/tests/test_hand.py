from day7.hand import Hand


def test_hand_value():
    # hand_1 = Hand("AA234")
    # assert hand_1.value() == 282

    hand_high_card_low = Hand("23456")
    assert hand_high_card_low.value() == 2*10000 + 3*1000 + 4*100 + 5*10 + 6*1

    hand_high_card_low_weird_ace = Hand("236A4")
    v1 = hand_high_card_low_weird_ace.value()
    assert v1 == 2*10000 + 3*1000 + 6*100 + 14 *10 + 4*1

    hand_high_card_low_last_ace = Hand("23745")
    v2 = hand_high_card_low_last_ace.value()
    assert v2 == 2*10000 + 3*1000 + 7*100 + 4*10 + 5*1

    assert v2 > v1

    hand_high_card_high = Hand("AKQJT")
    assert hand_high_card_high.value() == 14*10000 + 13*1000 + 12*100 + 11*10 + 10*1

    hand_pair_low = Hand("22345")
    assert hand_pair_low.value() == 200000 + 2*10000 + 2*1000 + 3*100 + 4*10 + 5*1

    hand_pair_high = Hand("AAKQJ")
    assert hand_pair_high.value() == 200000 + 14*10000 + 14*1000 + 13*100 + 12*10 + 11 *1

    hand_two_pair_low = Hand("22334")
    assert hand_two_pair_low.value() == 400000 + 2*10000 + 2*1000 + 3*100 + 3*10 + 4 *1

    hand_two_pair_low_reversed = Hand("33224")
    assert hand_two_pair_low_reversed.value() == 400000 + 3*10000 + 3*1000 + 2*100 + 2*10 + 4*1

    hand_two_pair_high = Hand("AAKKQ")
    assert hand_two_pair_high.value() == 400000 + 14*10000 + 14*1000 + 13*100 + 13*10 + 12*1


def test_hand_value_three_of_a_kind():
    hand_low = Hand("22234")
    assert hand_low.value() == 600000 + 2*10000 + 2*1000 + 2*100 + 3*10 + 4*1

    hand_high = Hand("AAAKQ")
    assert hand_high.value() == 600000 + 14*10000 + 14*1000 + 14*100 + 13*10 + 12*1

def test_hand_full_house():
    hand_low = Hand("22233")
    assert hand_low.value() == 800000 + 2*10000 + 2*1000 + 2*100 + 3*10 + 3*1

    hand_high = Hand("AAAKK")
    assert hand_high.value() == 800000 + 14*10000 + 14*1000 + 14*100 + 13*10 + 13*1

def test_hand_four_of_a_kind():
    hand_low = Hand("22223")
    assert hand_low.value() == 1000000 + 2*10000 + 2*1000 + 2*100 + 2*10 + 3*1

    hand_high = Hand("AAAAK")
    assert hand_high.value() == 1000000 + 14*10000 + 14*1000 + 14*100 + 14*10 + 13*1

def test_five_of_a_kind():
    hand_low = Hand("22222")
    assert hand_low.value() == 1200000 + 2*10000 + 2*1000 + 2*100 + 2*10 + 2*1

def test_boundary_conditions():
    h1 = Hand("AKQJT")
    h2 = Hand("22345")
    h3 = Hand("AAKQJ")
    h4 = Hand("22334")
    h5 = Hand("AAKKQ")
    h6 = Hand("22234")
    h7 = Hand("AAAKQ")
    h8 = Hand("22233")
    h9 = Hand("AAAKK")
    h10 = Hand("22223")
    h11 = Hand("AAAAK")
    h12 = Hand("22222")
    assert h1.value() < h2.value()
    assert h2.value() < h3.value()
    assert h3.value() < h4.value()
    assert h4.value() < h5.value()
    assert h5.value() < h6.value()
    assert h6.value() < h7.value()
    assert h7.value() < h8.value()
    assert h8.value() < h9.value()
    assert h9.value() < h10.value()
    assert h10.value() < h11.value()
    assert h11.value() < h12.value()