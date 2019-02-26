# Assignment 2
# ... Break the SHA1 Hashes ...
# By Farnoosh Sharifian Esfahani# This is The original Assignment without the optimized code.
# This provides solutions and codes to for all parts
# Part D takes a really long time to reach a solution. 
# run using the terminal command line 
import hashlib
import sys
import time
import threading
import Queue


def easyPassword(salt, passList, value, my_queue=None, addSpace=""):
    counter = 0
    done = False
    for password in passList:
        if addSpace:
            hashObject = hashlib.sha1(salt + addSpace + password.strip()).hexdigest()
            hashObjectR = hashlib.sha1(password.strip() + addSpace + salt).hexdigest()
        elif salt:
            hashObject = hashlib.sha1(salt + addSpace + password.strip()).hexdigest()
            hashObjectR = ""
        else:
            hashObject = hashlib.sha1(password.strip()).hexdigest()
            hashObjectR = ""
        counter= counter+1
        if hashObjectR:
            print "value: ", value
            print "hashObject: ", hashObject
            print "hashObjectR: ", hashObjectR
            if hashObject == value or hashObjectR == value:
                print salt, password
                my_queue.put(password, counter)
                global stop_thread
                if stop_thread:
                    return password, counter  #setting the found password to variable
        elif hashObject == value:
            return password, counter  #setting the found password to variable

            
    return None, None

def withSalt(counter, passList, value):
    salted, counter = easyPassword("", passList, salt)
    theCracked, counter = easyPassword(salted, passList, value)
    if theCracked:
        endTime = time.time() # end variable to calculate the end time of how long the program takes to crack the hash values.
        finalTime= endTime - startTime
    
        print("The Password is: "+ str(theCracked))
        print("Number of Tries: " +str(counter))
        print("It took the Program: " +str(finalTime) +" s.")
        return True




value = sys.argv[1] if len(sys.argv) == 2 else None
if not value:
    print "No Value given"
    exit()


startTime = time.time() # Start variable to calculate the time how long the program takes to crack the hash values.
counter = 0
theCracked = ""
salt = "f0744d60dd500c92c0d37c16174cc58d3c4bdd8e"

passList = []

with open("passwords.txt", 'r') as filehandle:
    # startTime = time.time() # Start variable to calculate the time how long the program takes to crack the hash values.
    for line in filehandle:
        counter+=1
        hashObject = hashlib.sha1(line.strip()).hexdigest()
        if hashObject == salt:
            salted = line.strip()
        elif hashlib.sha1(line.strip()).hexdigest() == value:
            theCracked = line.strip()            
            endTime = time.time() # end variable to calculate the end time of how long the program takes to crack the hash values.
            finalTime= endTime - startTime
            print("The Password is: "+ str(theCracked))
            print("Number of Tries: " +str(counter))
            print("It took the Program: " +str(finalTime) +" s.")
            break
        passList.append(line.strip())

if theCracked: exit()
if withSalt(counter, passList, value):
    exit()
else:
    my_queue = Queue.Queue()

    threads = []

    for i in range(len(passList)):
        t = threading.Thread(target=easyPassword, args=(passList[i], passList[i:], value, my_queue," "))
        threads.append(t)
        t.start()
    
    print my_queue.get()
    endTime = time.time() # end variable to calculate the end time of how long the program takes to crack the hash values.
    finalTime= endTime - startTime
    print("It took the Program: " +str(finalTime) +" s.")


