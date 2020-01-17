import sys
sys.path.append("/Users/Aditya/Desktop/functinal/LogicalPrograms")
import nibbles2
def test_nibbles():
    result=nibbles2.nibbles([1,1,0,0,1,0,0])
    assert result==70
