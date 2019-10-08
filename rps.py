#!/usr/bin/python2.7

import random

P = raw_input("Choose your move r|p|s: ")

C = random.randint(0,2)

print(P, 'vs', "rps"[C])

if P == "r" and C == 0:
    print("Tie")
if P == "r" and C == 1:
    print("You lose")
if P == "r" and C == 2:
    print("You win!")
if P == "p" and C == 0:
    print("You win!")
if P == "p" and C == 1:
    print("Tie")
if P == "p" and C == 2:
    print("You lose")
if P == "s" and C == 0:
    print("You lose") 
if P == "s" and C == 1:
    print("You win!")
if P == "s" and C == 2:
    print("Tie")
