"""
Ethan Dahlby (ed6tf), CS 3710 Programming Assignment #2, 11/12/2021
"""

import random
import math


def genPQ():  # Generating the unique random prime numbers p and q
    isPPrime = False
    isQPrime = False
    p = 0
    q = 0
    while p == q:
        while not isPPrime or p == q:
            p = random.randint(2, 10000)
            isPPrime = isPrime(p)
        while not isQPrime:
            q = random.randint(2, 10000)
            isQPrime = isPrime(q)
    return p, q


def isPrime(num):  # Does what it says on the tin, checks if a number is prime
    if num == 0 or num == 1:
        return False
    for check in range(2, int(math.sqrt(num)+1)):
        if num % check == 0:
            return False
    return True
# Got prime checking code from here: https://stackoverflow.com/questions/567222/simple-prime-number-generator-in-python


def compLambda(pNum, qNum):  # Computing lambda
    pPhi = pNum - 1
    qPhi = qNum - 1
    return lcm(pPhi, qPhi)


def lcm(x, y):  # Computing the Least Common Multiple of x and y
    if x >= y:
        greater = x
    else:
        greater = y
    while not (greater % x == 0 and greater % y == 0):
        greater += 1
    return greater
# LCM code from https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple


def findE(maxLambda):  # Finding e, which is a number less than lambda such that e and lambda are coprime
    testNum = maxLambda
    while not isPrime(testNum) or testNum == maxLambda:
        testNum = random.randint(2, maxLambda)
    return testNum


def bruteForceFindD(e, lambdaNum):  # Finding d, which is the modular multiplicative inverse of e modulo lambda
    i = 0
    while 1 != (i * e) % lambdaNum:
        i += 1
    return i


# This program gives a simple example of  RSA encryption and decryption process using a short numerical message
m = input("Input the message to encrypt (as an integer, please). ")
try:
    m = int(m)
except:
    print("Please restart the program and enter an int, not a string.")
    exit(-1)
generated = genPQ()
p = generated[0]
q = generated[1]
n = p*q
crowbar = compLambda(p, q)
e = findE(crowbar)
public = (n, e)  # The public key
d = bruteForceFindD(e, crowbar)
private = (n, d)  # The private key
encrypted = pow(m, e, n)  # To encrypt: message ^ e modulo n
decrypted = pow(encrypted, d, n)  # To decrypt: encrypted message ^ d modulo n

print("Original message: " + str(m))
print("p = " + str(p))
print("q = " + str(q))
print("n (p * q) = " + str(n))
print("lambda (lcm(p-1, q-1)) = " + str(crowbar))
print("e = " + str(e))
print("d = " + str(d))
print("Public key (n, e) = " + str(public))
print("Private key (n, d) = " + str(private))
print("Encrypted message: " + str(encrypted))
print("Decrypted message: " + str(decrypted))

# General source: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
