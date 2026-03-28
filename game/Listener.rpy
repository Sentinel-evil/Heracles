init python:
    import socket
    import json
    import threading
    host='127.0.0.1'
    port='5005'
    def network_listener(game_obj, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            sock.listen(1)

            while True:
                try:
                    conn, addr = sock.accept()
                    data = conn.recv(1024).decode('utf-8')
                    if data:
                        game_obj.apply_state(data)
                    conn.close()
                except:
                    print("Error in network listener. Continuing to listen for opponent.")
                    continue