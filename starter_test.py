# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

# test_oop_loan_pmt.py
import pytest
from oop_loan_pmt import Loan, collectLoanDetails, main 

@pytest.fixture
def loan():
    return Loan(100000, 30, 0.06)

# Unit tests
def test_discount_factor_calculation(loan):
    loan.calculateDiscountFactor()
    assert loan.getDiscountFactor() == pytest.approx(166.7916, rel=1e-4)

def test_loan_payment_calculation(loan):
    loan.calculateLoanPmt()
    assert loan.getLoanPmt() == pytest.approx(599.55, rel=1e-2)

# Functional tests
def test_collect_loan_details(monkeypatch):
    inputs = iter(['100000', '30', '0.06'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    loan = Loan(100000, 30, 0.06)
    assert loan.loanAmount == 100000
    assert loan.numberOfPmts == 360
    assert loan.annualRate == 0.06
    assert loan.periodicIntRate == 0.005

def test_main_function(capsys, monkeypatch):
    input_values = [10000, 30, 0.06]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    print("\r")
    print(" -- collectUserDetails functional test")
    loan = collectLoanDetails()
    assert loan.loanAmount == 10000
    assert loan.numberOfPmts == 360
    assert loan.annualRate == 0.06