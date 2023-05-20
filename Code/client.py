import socket
import colorama
from colorama import Fore, Style

SERVER = "127.0.0.1"
PORT = 10815 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))
print(Fore.RED+Style.BRIGHT+"Is there anything you would like to know about BINFO? (Type EXIT to close)")
while True:
    userInput = input(Fore.BLUE+"Question: ")

    if userInput == "EXIT":
        s.close()
        break

    s.sendall(userInput.encode())
    response = s.recv(1024).decode()
    print(Fore.GREEN+f"BINFO Info Bot: {response}")