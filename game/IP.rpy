init python:
    def get_my_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Doesn't actually connect, just probes the interface
            s.connect(('192.168.50.48', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '192.168.50.48'
        finally:
            s.close()
        return ip