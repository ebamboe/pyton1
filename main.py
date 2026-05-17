
def multiplication_or_sum(num1, num2):
    product = num1 * num2

    if product <=1000:
     return product
    else:
     return num1 + num2
result = multiplication_or_sum(30, 40)
print("The result is", result)
