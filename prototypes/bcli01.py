import os
import socket
import threading
import codecs
os.system("")
decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
sock = socket.create_connection(("www.windows93.net", 8082))
def receiver():
    while data := sock.recv(65536):
        print(decoder.decode(data), end="", flush=True)
threading.Thread(target=receiver, daemon=True).start()
while True:
    sock.sendall(input().encode("utf-8") + b"\r\n")
