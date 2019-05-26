import strcalculator

def test_EmptyStr():
    assert strcalculator.add("") == 0
    assert strcalculator.add("1,2,3") == (1 + 2 + 3)

def test_newline():    
    assert strcalculator.add("52, 1\n5678, 1, 1") == (52 + 1 + 5678 + 1 + 1)
def test_delimeters():    
    assert strcalculator.add(“//;2\n1;2;45;2") == (1 + 2 + 45 + 2)

def TestNegativeNumbers():
    with pytest.raises(Exception):
        assert strcalculator.add("//:\n-21:12\n4:-7:9")



