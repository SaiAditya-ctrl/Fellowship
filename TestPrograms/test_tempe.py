import sys
sys.path.append("/Users/Aditya/Desktop/bridge/Programming/Functional")
import anag
def test_temperature():
    result=anag.temperature('C',100)
    assert result==212
