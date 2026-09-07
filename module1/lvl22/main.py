# import asyncio
#
# def send_notification():
#     print("Відправляємо сповіщення!")
#
#
# async def send_message_later(loop, when):
#     loop.call_later(when, send_notification)
#
#     await asyncio.sleep(5)
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#
#     await send_message_later(loop, when=5)
#
#
#
# asyncio.run(main())


# import asyncio
# import time
#
# def send_midnight_alert():
#     print("Вітальна промова опівночі!")
#
# loop = asyncio.get_event_loop()
# # Отримуємо поточний час циклу подій і додаємо до нього 2 секунди
# when = loop.time() + 2
# loop.call_at(when, send_midnight_alert)
# loop.run_forever()
#
#
# import asyncio
#
# async def say():
#     print("C")
#
# async def main():
#     print("A")
#     asyncio.create_task(say())
#     print("B")
#
#
# asyncio.run(main())
#
# import asyncio
#
#
# async def worker():
#     print("WORKER: start")
#     await asyncio.sleep(1)
#     print("WORKER: end")
#     return "Hello"
#
#
# async def main():
#     print("MAIN: 1")
#
#     task = asyncio.create_task(worker())
#
#     await asyncio.sleep(0)
#
#     print("MAIN: 2")
#     print("MAIN: 3")
#
#     await task
#
#     print("MAIN: 4")
#
#
# asyncio.run(main())


#
# import asyncio
# async def long_running_task():
#     print("Задача почалась...")
#     await asyncio.sleep(5)
#     print("Задача завершена...")
#
#
# async def main():
#     task = asyncio.create_task(long_running_task())
#
#     await asyncio.sleep(6)
#     task.cancel()
#
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("Задача була скасована!")
#
# asyncio.run(main())

# import asyncio
#
# async def main():
#     task = asyncio.create_task(asyncio.sleep(1, result='Completed'))
#
#     result = await task
#     print(result) # Output: Completed
#
# asyncio.run(main())



# import asyncio
#
#
# async def worker():
#     await asyncio.sleep(2)
#     return 42
#
#
# async def main():
#     task = asyncio.create_task(worker())
#
#     print("1:", task.done())
#
#     await asyncio.sleep(1)
#
#     print("2:", task.done())
#
#     await asyncio.sleep(2)
#
#     print("3:", task.done())
#
#     print("Result:", task.result())


# asyncio.run(main())

# import asyncio
#
#
# async def broken():
#     await asyncio.sleep(1)
#     raise ValueError("Something went wrong")
#
#
# async def main():
#     task = asyncio.create_task(broken())
#
#     await asyncio.sleep(2)
#
#     print("Done:", task.done())
#     print("Exception:", task.exception())
#
#
# asyncio.run(main())


# import asyncio
#
# messages = []
#
# async def send_message(msg):
#     print("Sending message...")
#     messages.append(msg)
#     await asyncio.sleep(1)
#     print(f"Message '{msg}' was sent.")
#
# def callback(future):
#     print(f"You sent {len(messages)} message(s)")
#
# async def main():
#     task = asyncio.create_task(send_message("Hello!"))
#     task.add_done_callback(callback)
#     await task
#
#     task = asyncio.create_task(send_message("How are you?"))
#     task.add_done_callback(callback)
#     await task
#
# asyncio.run(main())