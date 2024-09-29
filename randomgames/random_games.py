import random
import string

class RandomStringGenerator:
    def __init__(self, length=8):
        self.length = length

    def generate(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(self.length))

class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
        while True:
            guess = int(input("Guess the number (between 1 and 100): "))
            self.attempts += 1
            if guess < self.number:
                print("Too low!")
            elif guess > self.number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {self.attempts} attempts.")
                break

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_palindrome(word):
    return word == word[::-1]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def print_tree(depth):
    for i in range(depth):
        print(' ' * (depth - i - 1) + '*' * (2 * i + 1))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def matrix_multiplication(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_val = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_val + shift) % 26 + shift_val)
        else:
            result += char
    return result

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    generator = RandomStringGenerator(12)
    print("Random String:", generator.generate())

    game = NumberGuessingGame()
    game.play()

    alice = Person("Alice", 25)
    alice.introduce()

    fib_seq = fibonacci(10)
    print("Fibonacci Sequence:", fib_seq)

    factors = prime_factors(56)
    print("Prime Factors of 56:", factors)

    word = "racecar"
    print(f"{word} is a palindrome: {is_palindrome(word)}")

    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array:", arr)

    print("Factorial of 5:", factorial(5))

    print("Tree:")
    print_tree(5)
