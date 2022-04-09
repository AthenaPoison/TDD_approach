"""
Employee class tests

Red phase: the starting point. It is used to write tests that informs
    the implementation of a feature. The test will only pass when expectations are met

    In this case, compute_payout() is not implemented and will return an error everytime it is called
"""

import unittest

from employee import Employee

NAME: str = "Athena"
EMPLOYEE_ID: int = 12345

class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute_payout method of the Employee class."""
    
    def setUp(self):
        #set up test first
        self.athena = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_a_float(self):
        #whether payout returns a float
        self.assertIsInstance(self.athena.compute_payout(), float)

    def test_employee_payout_no_commision_no_hours(self):
        #whether payout is correctly computed in case of 
        # no commision and no hours worked
        self.assertAlmostEqual(self.athena.compute_payout(), 1000.0)

    def test_employee_no_commision(self):
        #wheter payout is correctly computed in case of no 
        # commision and 10 hours worked
        self.athena.hours_worked =10.0
        self.assertAlmostEqual(self.athena.compute_payout(), 2000.0)

    def test_employee_payout_with_commision(self):
        #whether payout is correctly computed in case of 
        # 10 contracts landed in 10 hours worked
        self.athena.hours_worked = 10.0
        self.athena.contracts_landed = 10
        self.assertAlmostEqual(self.athena.compute_payout(), 3000.0)

    def test_employee_commision_disabled(self):
        #whether payout is correctly computed in case of 10 
        # contracts landed and 10 hours worked,
        # but comission is disabled
        self.athena.hours_worked = 10.0
        self.athena.contracts_landed = 10
        self.athena.has_commision = False
        self.assertAlmostEqual(self.athena.compute_payout(),3000.0)

if __name__ == "__main__":
    unittest.main()