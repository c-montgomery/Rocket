import asyncio
import time

async def async_test():
    asyncio.run()
    await asyncio.sleep(10,result='hello')
    print("fuck")
    time.sleep(8)

print("fuck")

async_test()
time.sleep(9)
