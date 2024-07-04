from nada_dsl import *

def secure_divide(secret_int, divisor):
    """Securely divide a SecretInteger by a public integer."""
    divisor_public = PublicInteger(divisor)
    return secret_int / divisor_public

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    # Secret integer inputs from each party
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))

    # Compute the sum
    sum_result = a + b + c
    
    # Compute the average (sum divided by 3)
    average_result = secure_divide(sum_result, 3)

    # Compute the maximum
    max_ab = If(a > b, a, b)
    max_result = If(max_ab > c, max_ab, c)

    # Output results to Party4
    return [Output(average_result, "average_output", party4), Output(max_result, "max_output", party4)]
