import socket
import colorama
from colorama import Fore, Style

def wrap(str, width):
    paragraphs = str.split("\n\n")
    lines = []
    words = []
    text = ""
    temp = ""
    terminalWidth = width
    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        for line in lines:
            words = line.split()
            for word in words:
                if len(temp) + len(word) < terminalWidth:
                    if temp == "":
                        temp = word
                    else:
                        temp = temp + " " + word
                elif len(word) > terminalWidth:
                    text = text + temp + "\n" + word + "\n"
                    temp = ""
                else:
                    text = text + temp + "\n"
                    temp = word
            if temp != "":
                text = text + temp + "\n"
            temp = ""
        text = text + "\n\n"
    return text


# Set up connection
SERVER = "127.0.0.1"
PORT = 10815 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

# Chat window
prompt = "Is there anything you would like to know about BINFO? (Type EXIT to close)"
print(Fore.RED+Style.BRIGHT+prompt)
while True:
    
    # Get input
    userInput = ""
    while userInput == "":
        userInput = input(Fore.BLUE+"Question: ")

    if userInput.lower() == "exit":
        s.close()
        break

    # Send and receive message
    s.sendall(userInput.encode())
    response = s.recv(32768).decode()
    response =f"BINFO Info Bot: \n{response}"
    
    response = wrap(response, len(prompt))

    # output response
    print(Fore.GREEN+response)
