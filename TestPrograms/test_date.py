import sys
sys.path.append("/Users/Aditya/Desktop/bridge/Programming/Functional")
import anag
def test_day():
    result=anag.day_of_week(1,16,2020)
    assert result=='sat'

    
