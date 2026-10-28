def prime_number_checker(num):
    if num < 2:
        return f"{num} is not a prime."
    number = 2
    prime_list = []
    is_prime = True
    sum = 0

    while number <= num:
        for i in range(2, number):
            if i * i <= number:
                if number % i == 0:
                    is_prime = False
                    break
            else:
                break
        if is_prime:
            sum += number
            prime_list.append(number)
        else:
            is_prime = True
        number += 1
    if num in prime_list:
        return f"""{num} is prime
Primes up to {num}: {prime_list}
sum of primes: {sum}"""
    else:
        return f"""{num} is not prime
Primes up to {num}: {prime_list}
sum of primes: {sum}"""


def main():
    print(prime_number_checker(10))
    print(prime_number_checker(7))
    print(prime_number_checker(2))
    print(prime_number_checker(3))
    print(prime_number_checker(4))


if __name__ == "__main__":
    main()
