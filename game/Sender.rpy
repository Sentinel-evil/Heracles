init python:
    import socket
    import json
    import threading
    def send_update(game_obj, target_ip, port=5005):
        def _send():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0)
                sock.connect((target_ip, port))
                sock.sendall(game_obj.get_state().encode('utf-8'))
                sock.close()
            except:
                print("Failed to send update to opponent. They may be offline.")
                pass # Silent fail if other player is offline
        
        # Run the send in a thread so the UI doesn't hitch
        threading.Thread(target=_send).start()