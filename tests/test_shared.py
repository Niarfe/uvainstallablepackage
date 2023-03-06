import sys
sys.path.append('.')
import shared as sh
import pytest

test_clean = [
    (" This! is      a ,test string  ", 'This is a test string'),
pytest.param(1234, "1234", marks=pytest.mark.xfail)  #expected to fail
]

@pytest.mark.parametrize('sample, expected', test_clean)
def test_clean_string(sample, expected): 
    assert sh.clean_string(sample) == expected
    assert sh.clean_string(sample) == expected

    
test_compress = [
    (" This! is      a ,test string  ", "This! is a ,test string"),
pytest.param(1234, "1234", marks=pytest.mark.xfail)  #expected to fail
]

@pytest.mark.parametrize('sample, expected', test_compress)
def test_space_compress(sample, expected): 
    assert sh.space_compress(sample) == expected
    assert sh.space_compress(sample) == expected
    

@pytest.mark.skip(reason = "can't test this")
def test_space_compress(): 
    assert sh.space_compress(45678) == "45678"

print("My platform is", sys.platform)
@pytest.mark.skipif(sys.platform == 'darwin', reason= "Test only for non-Macs")
def test_non_mac():
    print("My platform is", sys.platform)
    #assert sh.space_compress(45678) == "1234" #writing a failing test that will skip only on my platform
