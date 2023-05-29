# The BINFO Info Bot
The following is an overview of all Bot versions, which packages are needed, how they they should be run and how to use the client to connect to the bot.
Dependencies are to be installed before running the bot, for example with the Pip package manager.

## OpenAI version
This is the current version of the BINFO info Bot. 
### Dependencies
In order to be able to run the OpenAI version of the bot, only the following package is needed:
- openAI
### Running the Bot
Run the openAIBot python source file (openAIBot.py) in a terminal window. It will prompt when it is ready to accept connections. Use a keyboard interrupt to close the program.

## ChatterBot version
It is not recommended to run the ChatterBot version. It is depreciated, and relies on libraries that are as well. It is left here only for illustration purposes.
### Dependencies
In order to get the ChatterBot version to run, you need the following python packages:
- chatterbot
- chatterbot_corpus
- spaCy (which separateley needs to download the en_core_web_sm model)
It only runs on Python 3.8.0 and prior versions and the chatterbot source code needs to be adapted to handle newer spaCy nomenclature and calls.
### Running the Bot
Run the chatterBot python source file (chatterBot.py) in a terminal window. It will prompt when it is ready to accept connections.

## Client
### Running the client
Run the client python source file (client.py) in a terminal window. In order to successfully launch the client, an instance of the BINFO info Bot (any version) needs to be running on the same machine and be ready for connections. Type "exit" to properly close the client.
