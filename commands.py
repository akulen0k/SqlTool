"""

Класс, отвечающий за обработку пользовательских команд

"""
import configparser

from bfoutput import BfOutput
from database_commands import DatabaseTools


def read_settings():
    settings_path = "settings.ini"
    parser = configparser.ConfigParser()
    parser.read(settings_path)
    return parser["Development"]["PostgresOptions"]


class Commands:
    list_of_commands = ["show", "read", "clear", "execute"]

    def __init__(self):
        self.database = DatabaseTools(read_settings())

    @staticmethod
    async def get_command_from_string(command: str):
        command = command.split(' ', 1)
        command = [i.strip() for i in command]

        if len(command) == 0:
            raise Exception("Command is empty.")

        if command[0] not in Commands.list_of_commands:
            raise Exception(f"Command {command[0]} was not found.")

        return command

    async def execute_command(self, s: str):
        try:
            command = await Commands.get_command_from_string(s)
            if command[0] == Commands.list_of_commands[0]:   # show
                await self.get_tables()
            elif command[0] == Commands.list_of_commands[1]:
                await self.read_table(command[1])
            elif command[0] == Commands.list_of_commands[2]:
                await self.clear_table(command[1])
            elif command[0] == Commands.list_of_commands[3]:
                await self.execute_sql(command[1])
        except Exception as e:
            print(f"Exception occurred: {e}")

    async def get_tables(self):
        tables = await self.database.get_tables()
        BfOutput.print_tables(tables)

    async def read_table(self, dbname: str):
        table = await self.database.read_table(dbname)
        BfOutput.print_table(table)

    async def clear_table(self, dbname: str):
        await self.database.clear_table(dbname)

    async def execute_sql(self, sql: str):
        res = await self.database.execute_com(sql)
        if res is not None:
            BfOutput.print_table(res)