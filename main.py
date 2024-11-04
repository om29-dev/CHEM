import wifi
import server

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    for i in range(0,2):
        cl, addr = s.accept()
        print('Client connected from', addr)
        server.handle(cl)

start_server()