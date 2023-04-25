from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot and train it
binfoInfoBot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(binfoInfoBot)
trainer.train("chatterbot.corpus.english")

# Start the conversation
print("Is there anything you want to know about the Bachelor in Applied Information Technology?")
while True:
    try:
        userInput = input("Question: ")
        response = binfoInfoBot.get_response(userInput)
        print("BINFO Info Bot: ", response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break