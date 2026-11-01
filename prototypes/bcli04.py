import os
import asyncio
import threading
import codecs
import json
import telnetlib3
from datetime import datetime, timezone
os.system("")
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H_%M_%SZ")
decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
async def main():
    reader, writer = await telnetlib3.open_connection("www.windows93.net", 8082, encoding=False)
    loop = asyncio.get_running_loop()
    def sender():
        while True:
            loop.call_soon_threadsafe(writer.write, (input() + "\r\n").encode("utf-8"))
    threading.Thread(target=sender, daemon=True).start()
    with open(f"bcli04 server bytes log {stamp}.log", "wb") as stream_log, \
         open(f"bcli04 server packet log {stamp}.jsonl", "w", encoding="utf-8") as packet_log:
        while data := await reader.read(65536):
            stream_log.write(data)
            stream_log.flush()
            packet_log.write(json.dumps({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "content": data.decode("utf-8", errors="replace"),
                "bytes": data.hex(" "),
            }, ensure_ascii=False) + "\n")
            packet_log.flush()
            print(decoder.decode(data), end="", flush=True)
asyncio.run(main())