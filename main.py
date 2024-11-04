import wifi
import server
import moisture
from time import sleep as delay

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)
    cl, addr = s.accept()
    print('Client connected from', addr)
    for i in range(0,2):
        server.handle(cl)
    while True:
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(moisture.percent())
        cl.close()
        delay(1)

start_server()
