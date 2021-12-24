import socket
import multiprocessing as mp


def chat(conn, addr):
    while True:
        msg = conn.recv(1024).decode("utf-8")
        conn.send((msg + " too").encode("utf-8"))
        print(addr, ": ", msg)
    conn.close()


if __name__ == "__main__":
    sk = socket.socket()
    sk.bind(("127.0.0.1", 9000))
    sk.listen()
    print("start server 127.0.0.1:9000 ...")

    while True:
        conn, addr = sk.accept()
        mp.Process(target=chat, args=(conn, addr)).start()
    sk.close()
