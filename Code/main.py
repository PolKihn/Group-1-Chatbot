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

# Define user interaction
def handleClient(clientSocket, clientAddress):
    print(f"{clientAddress} connected.")
    while True:
        userInput = clientSocket.recv(1024).decode()

        if not userInput:
            print(f"{clientAddress} disconnected.")
            clientSocket.close()
            break

        botOutput = binfoInfoBot.get_response(userInput)
        response = f"{botOutput}"
        clientSocket.send(response.encode())

# Start server
serverSocket.listen()
print("BINFO Info Bot ready. Awaiting connections.")
while True:
        clientSocket, clientAddress = serverSocket.accept()
        clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress))
        clientThread.start()