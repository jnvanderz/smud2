import os
import asyncio
import threading
import telnetlib3
os.system("")
async def main():
    reader, writer = await telnetlib3.open_connection("www.windows93.net", 8082, encoding="utf-8")
    loop = asyncio.get_running_loop()
    def sender():
        while True:
            loop.call_soon_threadsafe(writer.write, input() + "\r\n")
    threading.Thread(target=sender, daemon=True).start()
    while data := await reader.read(65536):
        print(data, end="", flush=True)
asyncio.run(main())