# Python Boardgame Server

This is a program that will act as a simple boardgame server for multi-player games written on low end platforms like 8 bit machines.

## Motivation

In particular, I'm writing this with the Atari 8 bits using the [Fujinet](https://fujinet.online/) SIO network adapter. However this is in no way tied to that :)

## Implementation

Since we're modeling physical objects (board games) OO fits well here.

### Transport

The serve ruses regular old sockets. I thought about creating a REST API but given that the goal is to create something that's accessible to low end computers that seemed like a lot of extra overhead for sending a few commands and parameters down the pipe in a very low bandwidth way.

## Using the server

TODO: Add more detail

Commands:

- register_game <game_type> e.g. tictactoe

- register_player <player_number> <name>

- place_piece <x,y>

- end_game <winner>
