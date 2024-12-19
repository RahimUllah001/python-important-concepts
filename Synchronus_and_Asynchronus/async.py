import asyncio
import time
async def task_1():
    print("Starting task 1")
    await asyncio.sleep(3)  # Simulating a task that takes 3 seconds
    print("Task 1 done")

async def task_2():
    print("Starting task 2")
    await asyncio.sleep(2)  # Simulating another task that takes 2 seconds
    print("Task 2 done")

# Run tasks concurrently
async def main():
    await asyncio.gather(task_1(), task_2())

# Start the async tasks
asyncio.run(main())
