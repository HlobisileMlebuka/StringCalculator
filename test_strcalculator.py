import strcalculator
import pytest

def test_EmptyStr():
    assert strcalculator.add("") == 0
    
def test_newline():    
    assert strcalculator.add("52, 1\n5678, 1, 1") == (52 + 1 + 1 + 1)

def test_delimeters(): 
        # import pdb
        # pdb.set_trace()
        with pytest.raises(Exception):     
                assert strcalculator.add("//45;\n245;-145;245;2000") == (2 + 1 + 2 )
                assert strcalculator.add("//45;\n245;145;245;2000") == (2+1+2)
def testNegativeNumbers():
        # import pdb
        # pdb.set_trace()
        with pytest.raises(Exception):
                assert strcalculator.add("21,12\n,4,-7,9")

def testMassiveNumbers():
        assert strcalculator.add("//;\n1;2\n;5;1200") == (1 + 2 + 5)

def testAnyLengthDelimeter():
        assert strcalculator.add("//&&&\n1&&&5&&&6") == (1 + 5 + 6)

def testMultipleDelimeter():
        assert strcalculator.add("//[&][*][$]\n1*56$1&") == (1 + 56 + 1)

