from boardgameserver import BoardGameServer
from socket import create_connection

def test_server_is_listening():
    # Use default host and port
    bgs = BoardGameServer()

    # Now make a client connection to see if we're listening :)
    conn = create_connection((bgs.host, bgs.port))
    # Just make sure it's not none. create_connection raises on error.
    assert conn

