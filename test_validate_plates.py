import unittest
from validate_plates import validate_plates

CNF = 'brasil.cnf'

class TestValidadePlates(unittest.TestCase):
    def tests(self):
        assert validate_plates(CNF, 'Abc123')  == True
        assert validate_plates(CNF, '123')     == False
        assert validate_plates(CNF, 'a1b2c3')  == True
        assert validate_plates(CNF, '5555aa')  == False
        assert validate_plates(CNF, 'ghi999')  == True
        assert validate_plates(CNF, 'abcd123') == False
        assert validate_plates(CNF, 'TTT000')  == True
        assert validate_plates(CNF, '+88hhh')  == False
        assert validate_plates(CNF, 'Qua890')  == True
        assert validate_plates(CNF, 'abCD6x')  == False