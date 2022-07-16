import socket
import typer

board_sizes = {
    'checkers': 8,
    'go': 19,
    'othello': 8
}


def register_game(self, game: str):
    game_state = {
        'board_size': board_sizes[game],
        'game': game,
    }


def boardgameserver(self):
    if __name__ == '__main__':
        typer.run(boardgameserver)
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 8907  # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                conn.send(b"Would you like to play a game?\n")
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    match data.split():
                        case ["play", game]:
                            register_game(game)
                        case ["end"]:
                            end_game()
                        case ["place",x,y]:
                            place(x,y)
                        case ["remove",x,y]:
                            remove(x,y)
                    

                
                

