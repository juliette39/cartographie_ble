import uasyncio as asyncio
import aioble

print("Hello World")

async def main():
    async with aioble.scan(duration_ms=5000) as scanner:
        async for result in scanner:
            print(result, result.name(), result.rssi, result.services())

asyncio.run(main())