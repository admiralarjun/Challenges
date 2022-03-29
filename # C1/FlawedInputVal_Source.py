from cgitb import reset
import urllib.parse
import sys
from time import sleep

key = '"><script>alert("foo")</script>'

intro = '''
Welcome to the challenge! Instructions are 
straightforward - You will be given a "key",
smuggle it through air tight validation process
Good luck!

Peek into validations:
[+] Enter payload that can be smuggled
[+] <script> will be deleted
[+] Double quotes will be deleted
[+] URL-Decode will be done on the input
'''
print(intro+"\n")
print('key = "><script>alert("foo")</script>\n')

CongoMessage = '''
Congratulations!

You successfully cracked this challenge.
Here is the lead to your next challenge.
Follow @admiralarjun - Twitter/Instagram/Telegram - Everywhere!

VISIT: https://admiralarjun.com

Good luck - Happy Hacking!
'''

# ------------------------------------

def printCongo():
    for char in CongoMessage:
        sleep(0.1)
        print(char,end="")
        sys.stdout.flush()

def outLog(payload):
    print("Your output: "+payload)
    print("Expected output: "+key)

def ripper():
    payload = input("Enter the bypassable payload: ")
    payload = payload.replace("<script>", "")
    payload = payload.replace('"', "")
    payload = urllib.parse.unquote(payload)

    if(payload == key):
        printCongo()
        exit(1)
    else:
        print("Try harder!!!\n")  
        print(outLog(payload))
        sleep(2)
        ch = input("Press ENTER to try again")
        if(ch == "\n"):
            ripper()

ripper()
