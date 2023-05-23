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

# Provide context, and uni data for the bot
def botContext():
    with open(os.path.join(os.path.dirname(__file__),"..","Binfo Source File","openAI.txt"), "r", encoding="utf-8") as file:
        uniData = file.read()
    context = []
    context.append({
        "role":"system","content":"You are the BINFO Info Bot. The following text is the content of the website of the Univerity of Luxembourg, giving information about the Bachelor in applied Information Technology (BINFO)."
    })
    context.append({
        "role": "system", "content": uniData
    })
    return context


# Generate a response from the chatbot
def answer(query):
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

    # Set context at the beginning of the exchange
    history = botContext()
    
    # Start chat
    while True:
        userInput = clientSocket.recv(32768).decode()

        if not userInput:
            print(f"{clientAddress} disconnected.")
            clientSocket.close()
            break

        history.append({"role": "user", "content": userInput})
        
        try:    
            response = answer(history)
        except openai.error.InvalidRequestError:
            history = botContext()
            history.append({"role": "user", "content": userInput})
            response = answer(history) + "\n\n Unfortunately, due to an formatting error, possibly due to size constraints, I had to reset the context of our conversation. I won't be able to remeber our previous exchange."
        except openai.error.RateLimitError:
            response = "Please wait up to 20 seconds, before asking me another question. There is unfortunately a limit to the rate at which I can answer questions."
        except openai.error.APIError:
            response = "There was a problem processing your question. Please ask again, and if the error persists, try again later."

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