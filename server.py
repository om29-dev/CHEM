import wifi
# Handle HTTP requests
def handle_client(client):
    request = client.recv(1024)
    request = str(request)

    if '/connect' in request:
        ssid_start = request.find('ssid=') + 5
        ssid_end = request.find('&', ssid_start)
        ssid = request[ssid_start:ssid_end].replace('%20', ' ')
        
        password_start = request.find('password=') + 9
        password_end = request.find(' ', password_start)
        password = request[password_start:password_end].replace('%20', ' ')
        
        wifi.connect(ssid, password)

        # Check internet connection
        if check_internet():
            response = "Connected to {} successfully!".format(ssid)
        else:
            response = "Failed to connect to internet."
        
        client.send('HTTP/1.1 200 OK\nContent-Type: text/plain\n\n{}'.format(response))
    else:
        networks = scan_wifi()
        html_content = read_html_file()
        options = ''.join(f'<option value="{ssid.decode()}">{ssid.decode()}</option>' for ssid, *_ in networks)
        html_content = html_content.replace('<select name="ssid">', f'<select name="ssid">{options}')
        
        client.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n{}'.format(html_content))
    
    client.close()
