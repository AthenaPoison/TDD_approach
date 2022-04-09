"""
Employee management system
"""
from dataclasses import dataclass

@dataclass
class Employee:
    #basic representation of an employee

    name: str
    employee_id: int
    pay_rate:float = 100.0
    hours_worked: float = 0.0
    employer_cost:float = 1000.0
    has_commision: bool = True
    commision: float =100.0
    constracts_landed: int = 0

    def compute_payout(self) -> float:
        #compute how much the employee should be paid
        raise NotImplementedError()