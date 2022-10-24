
#//---LIBRARIES---//
#Keep this in mind: you need to install StringGenerator 0.4.4 version from the python packages in your ID. Most IDs come with pre installed libs such as os, threading, ctypes and base64
import ctypes, os, threading, strgen, base64
#this has to be here, if no, python will totally ignore the existence of StringGenerator in strng library
from strgen import *
from strgen import StringGenerator

tokenid = "INSERT TOKEN ID"

#another amazing note: keep in mind that you are responsible for the shit u are plannin to do with this piece of code, not me

class Discord:
    def __init__(self):
        self.regularExpression = ".([a-zA-Z0-9]{6})\.([a-zA-Z0-9]{38})"
        self.generated = 0

    def generate(self):
        discordToken = strgen.StringGenerator(self.regularExpression).render() #generating the tokens from the ID
        discordToken = discordToken.replace("..", ".")
        discordToken = str(id) + discordToken 
        print(discordToken)
        self.generated += 1
        self.write(discordToken)
        self.title()

    def new_method(self):
        return self.regularExpression
    
    def write(self, discordToken):
        if os.path.isfile("./tokens.txt"):
            writeToken = open("./tokens.txt", "a")
            writeToken.write(f"{discordToken}\n")
        else:
            open("./tokens.txt", "w").close() #this amazing part creates txt file with your tokens if you want to do straight up hacking stuff

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"DBF FEPO :)  : {self.generated}")


open("./tokens.txt", "w").close() 
token = Discord()
amountToGen = int(input("Enter amount of tokens to generate: "))

#encoding the token into base64 (for more info, check : https://docs.python.org/3/library/base64.html)
id = base64.b64encode((input("Enter ID: ")).encode("ascii"))
id = str(id)[2:-1]

for _ in range(amountToGen):
    threading.Thread(target=token.generate).start()
