import sys
sys.path.append("/Users/Aditya/Desktop/bridge/Programming/Functional")
import anag
def test_payment():
    result=anag.payment(100,2,2)
    assert result==199
