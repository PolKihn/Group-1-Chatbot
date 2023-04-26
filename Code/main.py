from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import socket
import threading

# Configure the server socket
HOST = "127.0.0.1"    # Default loopback adress
PORT = 10815
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))

# Create a new chat bot and train it
binfoInfoBot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(binfoInfoBot)
trainer.train("chatterbot.corpus.english")

# Generate a response from the chatbot
def answer(query):
     return f"{binfoInfoBot.get_response(query)}"

# Define user interaction
def handleClient(clientSocket, clientAddress):
    print(f"{clientAddress} connected.")
    while True:
        userInput = clientSocket.recv(1024).decode()

        if not userInput:
            print(f"{clientAddress} disconnected.")
            clientSocket.close()
            break

        response = answer(userInput)
        clientSocket.send(response.encode())

# Start server
serverSocket.listen()
print("BINFO Info Bot ready. Awaiting connections.")
while True:
        clientSocket, clientAddress = serverSocket.accept()
        clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress))
        clientThread.start()