import socket
from _thread import start_new_thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]


def threaded_client(server_conn):
    global currentId, pos, nid
    server_conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = server_conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                server_conn.send(str.encode("Goodbye"))
                break
            else:
                print("Received: " + reply)
                arr = reply.split(":")
                pos_id = int(arr[0])
                pos[pos_id] = reply

                if pos_id == 0: nid = 1
                if pos_id == 1: nid = 0

                reply = pos[nid][:]
                print("Sending: " + reply)

            server_conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    server_conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
