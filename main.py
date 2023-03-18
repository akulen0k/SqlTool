import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

from commands import Commands


async def main():
    handler = Commands()

    while True:
        s = input()
        if s == "exit":
            return

        await handler.execute_command(s)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
