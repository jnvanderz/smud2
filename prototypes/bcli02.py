# minimal client that connects to www.windows93.net 8082 using sockets only
# logs everything the server responds in 2 files
#    server bytes log <- the entire contents of the server response stream
#    server packet log <- it wraps the exact packet the way it arrived at this client, and timestamps it
#        so we can see that not every packet ends with a \n
import os
import socket
import threading
import codecs
from datetime import datetime, timezone
import json
os.system("")
decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
sock = socket.create_connection(("www.windows93.net", 8082))
stream_log = open(f"bcli02 server bytes log {datetime.now(timezone.utc).strftime("%Y-%m-%d_%H_%M_%SZ")}.log","wb")
packet_log = open(f"bcli02 server packet log {datetime.now(timezone.utc).strftime("%Y-%m-%d_%H_%M_%SZ")}.log","w",encoding="utf-8")
def receiver():
    while data := sock.recv(65536):
        stream_log.write(data)
        stream_log.flush()
        line = json.dumps({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "content": bytes(data).decode("utf-8", errors="replace"),
            "bytes": data.hex(" "),
        }, ensure_ascii=False)
        packet_log.write(line)
        packet_log.write("\r\n")
        packet_log.flush()
        print(decoder.decode(data), end="", flush=True)
    os._exit(0)
threading.Thread(target=receiver, daemon=True).start()
try:
    while True:
        sock.sendall(input().encode("utf-8") + b"\r\n")
except (KeyboardInterrupt, EOFError):
    pass
stream_log.close()
packet_log.close()
