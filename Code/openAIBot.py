# pip install openAI

import socket
import threading
import os
import openai
import sys

# Configure the server socket
HOST = "127.0.0.1"    # Default loopback adress
PORT = 10815
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.settimeout(1.0)
serverSocket.bind((HOST, PORT))

# Configure Bot
API_key_encoded = [115, 107, 45, 81, 50, 80, 111, 90, 72, 109, 99, 56, 101, 115, 65, 68, 80, 120, 90, 89, 122, 86, 51, 84, 51, 66, 108, 98, 107, 70, 74, 66, 55, 85, 97, 114, 99, 114, 85, 54, 49, 105, 101, 86, 103, 108, 69, 56, 89, 99, 80]
API_key_plain = ""
for i in API_key_encoded:
    API_key_plain = API_key_plain + chr(i)
openai.organization = "org-fG1iZAd4wN07PkkA6iDC4RDb"
openai.api_key = API_key_plain
openai.Model.list()


# Generate a response from the chatbot
def answer(query):
    
    # Generate a response from the chatbot
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=query,
        temperature=0.2,
    )


    reply = response["choices"][0]["message"]["content"]
    return reply

# Define user interaction
def handleClient(clientSocket, clientAddress):
    
    print(f"{clientAddress} connected.")

    # Set context

    with open(os.path.join(os.path.dirname(__file__),"..","Binfo Source File","openAI.txt"), "r", encoding="utf-8") as file:
        uniData = file.read()
    history = []
    history.append({
        "role":"system","content":"The following text is the content of the website of the Univerity of Luxembourg, giving information about the Bachelor in applied Information Technology (BINFO). All user questions relate to it. Reference it to answer them."
    })
    history.append({
        "role": "system", "content": uniData
    })
    
    # Start chat
    while True:
        userInput = clientSocket.recv(1024).decode()

        if not userInput:
            print(f"{clientAddress} disconnected.")
            clientSocket.close()
            break
        
        history.append({"role": "user", "content": userInput})    
        response = answer(history)
        history.append({"role": "assistant", "content": response})
        clientSocket.send(f"{response}".encode())

# Start server
serverSocket.listen()
print("BINFO Info Bot ready. Awaiting connections.")
while True:
    try:
        clientSocket, clientAddress = serverSocket.accept()
        clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress), daemon=True)
        clientThread.start()
    except  socket.timeout: {}    
    except KeyboardInterrupt:
        sys.exit()

# py ./code/client.py