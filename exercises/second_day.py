from math import sqrt

def fizzer(num):
    if num % 15 == 0:
        print ("Fizzbuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)

#for i in range(31):
#    fizzer(i)

def is_prime(num):
    """
        returns true if number is prime,
        returns false otherwise
    """
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num // 2, 2):
            if num % i == 0:
                return False
        return True

def largest_prime():
   num = 600851475143
   i = 2
   while i * i < num:
       while num % i == 0:
           num = num / i
       i = i + 1
   return num
print (largest_prime())

def print_str(str):
    for i in range(len(str)):
        print(str[i])
#print_str("abusimbel")

def print_vowel(str):
    vowel = "aeiou"
    for i in range(len(str)):
        if str[i].lower() in vowel:
            print(str[i],)
#print_vowel("abusimbel")

def print_consonants(str):
    vowel = "aeiou"
    for i in range(len(str)):
        if str[i].lower() not in vowel:
            print(str[i],)
#print_consonants("abusimbel")