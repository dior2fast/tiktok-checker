import requests
import random
import string

def get_random_stringa(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_stringn(length):
    letters = string.ascii_lowercase
    numbers = string.digits
    result_str = ''.join(random.choice(letters + numbers) for i in range(length))
    return result_str



a = open('usernames.txt', 'a+')
try:
    ad = input("[!] Name Starts With (Leave Blank For Random) : ")
    am = int(input("[!] Amount Of Letters : "))
    d = int(input("[!] Amount To Generate : "))
    incnum = input("[!] Include Numbers (y/n): ")

except:
    print("Please enter a valid number!")
if incnum == "y":
    while d > 0:
        ca = am - len(ad)
        n = ad + get_random_stringn(ca)
        a.write(n + "\n")
        d -= 1
elif incnum == 'n':
    while d > 0:
        ca = am - len(ad)
        n = ad + get_random_stringa(ca)
        a.write(n + "\n")
        d -= 1
else:
    print("[!] Please enter a valid option!")
