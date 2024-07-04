from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    # Secret integer inputs from each party
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))

    # Compute the sum and product
    sum_result = a + b + c
    product_result = a * b * c

    # Output results to Party4
    return [Output(sum_result, "sum_output", party4), Output(product_result, "product_output", party4)]
