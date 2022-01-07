[![Nodejs-CI](https://github.com/SriMethan/Liantichess/actions/workflows/nodejs.yml/badge.svg)](https://github.com/SriMethan/Liantichess/actions/workflows/nodejs.yml)

## Liantichess

Liantichess is a free, open-source antichess server designed to play antichess variants.

Currently supported games are:

- [Antichess](https://liantichess.herokuapp.com/variants/antichess)
- [Antichess960](https://liantichess.herokuapp.com/variants/antichess960)

Additionally you can check Chess960 option in for Antichess
[Chess960 castling rules](https://en.wikipedia.org/wiki/Chess960#Castling_rules)

For move generation, validation, analysis and engine play it uses
- [Fairy-Stockfish](https://github.com/ianfab/Fairy-Stockfish)
- [fairyfishnet](https://github.com/gbtami/fairyfishnet) fork of [fishnet](https://github.com/niklasf/fishnet)
- [lichess-bot-variants](https://github.com/gbtami/lichess-bot-variants) fork of [lichess-bot](https://github.com/careless25/lichess-bot)

On client side it is based on
[chessgroundx](https://github.com/gbtami/chessgroundx) fork of [chessground](https://github.com/ornicar/chessground)

##

liantichess is a free server and it will remain free forever.

## Installation

### Prerequisites
* You need mongodb up and running. [Mongo daemon](https://docs.mongodb.com/manual/installation/)


### Project setup
```
pip3 install -r requirements.txt --user // Install python requirements
yarn install                            // Install node requirements
yarn dev                                // Compile typescript files to javascript
yarn md                                 // Compile md files to html
```

### Start server
```
python3 server/server.py
```

## Open in GitPod

GitPod lets you configure one off initializing tasks and tasks that should be run on each startup.

The project comes with the necessary GitPod config files that instruct GitPod to install dependencies for the first time, and on every startup start MongoDb and the dev server.

You can open the repo in GitPoe by attaching the repo url to `https://gitpod.io/#`. For this concrete fork the url would be:

[https://gitpod.io/#https://github.com/easychessanimations/Liantichess](https://gitpod.io/#https://github.com/easychessanimations/Liantichess)

For the first time the server won't start as the installation will be still ongoing. So wait for the installation to finish and in the `Run Server` terminal tab type `. startserver.sh` or simply bring back this command with the up arrow and now the server will start ok.

You can also set the server URI in https://gitpod.io/variables, Create a variable `LIATOMIC_URI` and set it to the web page url as opened by GitPod for the server, without the trailing slash and change protocol to `http`. The startserver script will export this variable as `URI` so that redirect for oauth will be correct.

Example `LIATOMIC_URL`:

`http://8080-amber-reindeer-qu3afegt.ws-eu25.gitpod.io`