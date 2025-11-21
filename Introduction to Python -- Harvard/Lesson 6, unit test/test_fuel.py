from fuel import convert, gauge

def test1():
    assert convert(3) == 300
    assert convert(0.5) == 50
    assert convert(0.01) == 1

def test2():
    assert gauge(70) == "70%"
    assert gauge(10) == "10%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
