import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8907  # Port to listen on (non-privileged ports are > 1023)

class BoardGameServer:

    def __init__(self, host=HOST, port=PORT):

        self.host = host
        self.port = port

        self.board_sizes = {
            'checkers': 8,
            'go': 19,
            'othello': 8
        }


    def create_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                conn.send(b"Would you like to play a game?\n")
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    self.parse_command(data)


    def parse_command(self, data):
        match data.split():
            case ["play", game]:
                self.register_game(game)
            case ["end"]:
                self.end_game()
            case ["place",x,y]:
                self.place_piece(x,y)
            case ["remove",x,y]:
                self.remove_piece(x,y)




    def register_game(self, game: str):
        game_state = {
            'board_size': self.board_sizes[game],
            'game': game,
        }

    def end_game(self):
        pass

    def place_piece(self, x,y):
        pass

    def remove_piece(self):
        pass


def main():
    bgs = BoardGameServer()
    bgs.create_server()

if __name__ == '__main__':
    main()
