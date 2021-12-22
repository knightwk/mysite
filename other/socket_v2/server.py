import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()
print("start server 127.0.0.1:9000 ...")
conn, addr = sk.accept()

while True:
    msg = conn.recv(1024).decode("utf-8")
    conn.send((msg + " too").encode("utf-8"))
    print(addr, ": ", msg)
conn.close()