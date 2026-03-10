from ndfl.tax import calculate_tax


def test_basic_ndfl():
    assert calculate_tax(200_000) == 26_000


def test_ndfl_tier_2():
    assert calculate_tax(3_000_000) == 402_000


def test_ndfl_tier3():
    assert calculate_tax(7_000_000) == 1_062_000


def test_ndfl_tier4():
    assert calculate_tax(30_000_000) == 5_402_000