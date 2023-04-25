import socket

SERVER = "127.0.0.1"
PORT = 10815 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))
print("Is there anything you would like to know about BINFO? (Type EXIT to close)")
while True:
    userInput = input("Question: ")

    if userInput == "EXIT":
        s.close()
        break

    s.sendall(userInput.encode())
    response = s.recv(1024).decode()
    print(f"BINFO Info Bot: {response}")