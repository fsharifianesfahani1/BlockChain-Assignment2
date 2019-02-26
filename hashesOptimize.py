# Assignment 2

# ... Break the SHA1 Hashes ...

# By Farnoosh Sharifian Esfahani
# The Optimized solution for this assignment.
# Removed excess of for loops and use of lists
# Made Part C ALOT faster than the other code.
# run using the terminal command line 

import hashlib
import sys
import time

value = sys.argv[1] if len(sys.argv) == 2 else None
if not value:
    print "No Value given"
    exit()

theCracked = ""
salt = "f0744d60dd500c92c0d37c16174cc58d3c4bdd8e"
startTime = time.time() # Start variable to calculate the time how long the program takes to crack the hash values.
def openFile(value, salt="", salted="", counter=0):
    with open("passwords.txt", 'r') as filehandle:
        for line in filehandle:
            counter += 1
            hashObjectWithSalt = hashlib.sha1(salted + line.strip()).hexdigest()
            hashObject = hashlib.sha1(line.strip()).hexdigest()
            if salt and hashObject == salt:
                salted = line.strip()
            if hashObject == value or hashObjectWithSalt == value:
                return salted, value, line.strip(), counter
    return salted, value, None, counter



salted, value, theCracked, counter = openFile(value, salt)
if theCracked:
    endTime = time.time() # end variable to calculate the end time of how long the program takes to crack the hash values.
    finalTime= endTime - startTime
    print("The Password is: "+ str(theCracked))
    print("It took the Program: " +str(finalTime) +" s.")
    print("Number of Tries: " +str(counter))
else:
    theCracked = " Not Found. "
    endTime = time.time()  # end variable to calculate the end time of how long the program takes to crack the hash values.
    finalTime = endTime - startTime
    print("The Password is: " + str(theCracked))
    print("It took the Program: " + str(finalTime) + " s.")
    print("Number of Tries: " + str(counter))
