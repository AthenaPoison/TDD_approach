"""
Employee management system

Refactor phase: Where you begin thinking about improvements.
    In this phase you are "in the green"
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
    commision: float =100.0
    constracts_landed: int = 0

    #Here we add a has commision method using conditionals to check
    #if there are commisions
    def has_commision(self) -> bool:
        #whether the employee has a commision
        return self.commision > 0

    def compute_payout(self) -> float:
        
        payout = self.pay_rate * self.hours_worked + self.employer_cost
        if self.has_commision:
            payout += self.commision * self.constracts_landed
        return payout