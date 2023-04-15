#Title/Header Section
import pyfiglet
from colorama import Fore, Back, Style
print(Fore.BLUE + pyfiglet.figlet_format("  The  Vigenère  Cipher   ", font = "xsansb", width=500))

#Welcome Message
from pyboxen import boxen
print(
        boxen(
            "This program will help you in converting plaintext and keyword into ciphertext using the Vigenère Cipher.",
            color="bold blue",
        )
    )

#Ask the user the message string and the key string
#List the letter values that will be used in translating the plaintext inputted by the user
#Use the number substitute to turn each element by its corresponding number
#Get the sum of each elements from message and key which are aligned in column, then the mod 26 of each sum
#Encrypt
#Processing the Output/Loading
#Display the decrypted text to the user
#Ask the user if he/she wants to try again the program.