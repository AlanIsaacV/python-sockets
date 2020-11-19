# Python Sockets TCP

## How does it work

Implementation of python sockets to communicate a server with multiples clients.

The server implement multi-theading for manament each message for the clients.

Each request send two parts, the header and the message (The message can be anything, it can be any object of python or a json).
The Header is declared indicate the `HEADERSIZE`

## Prerequisite

To validate the functionality you only need to have installed **Docker** and **docker-compose**

## Run

If you want to validate that the module works, you just have to run `docker-compose up` this create two images and run it.

### *Images*

**client** Send a *test.json* to server using the socket and recives a message if json was recive successfully

**Server** This run the socket server it recives the message from the client (A json file) and save it, if json file is saved successfully send message to recived to the client
