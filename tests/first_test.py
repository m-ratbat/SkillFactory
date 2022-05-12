import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 3) == 2

    def test_division_calculation_failed(self):
        assert self.calc.division(self, 0, 2) == 1

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_subtraction_calculation_failed(self):
        assert self.calc.subtraction(self, 7, 2) == 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 3) == 8

    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 4, 5) == 1

