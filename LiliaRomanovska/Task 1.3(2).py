number = int(input("Please enter a number: "))


def divisor_s():
    divisors = []
    for i in range(number, 0, -1):
        if number % i == 0:
            divisors.append(i)
    return sorted(divisors)


print(divisor_s())
