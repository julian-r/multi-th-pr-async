import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection("127.0.0.1", 1234)
    for i in range(100):
        await asyncio.sleep(0.1)
        writer.write('message'.encode())
    writer.close()

async def client():
    clients = []
    for num in range(1000):
        clients.append(tcp_echo_client())
    
    await asyncio.gather(*clients)


loop = asyncio.get_event_loop()
loop.run_until_complete(client())
loop.close()
