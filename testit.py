import shared as sh
sh.afunction()

def test_multi_spaces():
    assert sh.space_compress('word       word     word') == 'word word word', "Failed multi space"


def test_multi_lines():
    multiline = """
    word
    word
    word
    """
    assert sh.space_compress(multiline) == 'word word word', "Failed multi line"


def test_assert_int():
    with pytest.raises(Exception) as exc_mssg:
        sh.space_compress(2)

    assert "Expected str but got" in str(exc_mssg)
    assert "int" in str(exc_mssg)


def test_assert_bool():
    with pytest.raises(Exception) as exc_mssg:
        sh.space_compress(False)

    assert "Expected str but got" in str(exc_mssg)
    assert "bool" in str(exc_mssg)
