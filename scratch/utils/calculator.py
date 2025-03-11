def calculate_monthly_payment(principal: int, rate: float, term: int):
    pmt = (principal * (1 + rate) ** (term / 12)) / term
    return pmt
