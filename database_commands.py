"""

Класс, отвечающий за работу с базами данных
При создании должен просить connectionString
Операции:
    1) Получить список всех доступных баз
    2) Прочитать базу данных

"""
import psycopg


class DatabaseTools:

    def __init__(self, con_string: str):
        self.connection_string = con_string

    async def get_tables(self):
        async with await psycopg.AsyncConnection.connect(
                self.connection_string) as con:
            rows = await con.execute("""SELECT table_name FROM information_schema.tables
                   WHERE table_schema = 'public'""")
            return await rows.fetchall()

    async def read_table(self, table_name: str):
        async with await psycopg.AsyncConnection.connect(
                self.connection_string) as con:
            rows = await con.execute("""SELECT * FROM %s""" % table_name)
            columns = [i[0] for i in rows.description]
            columns = [tuple(columns)]
            rows = await rows.fetchall()
            return columns + rows

    async def clear_table(self, table_name: str):
        async with await psycopg.AsyncConnection.connect(
                self.connection_string) as con:
            await con.execute("TRUNCATE TABLE %s" % table_name)

    async def execute_com(self, sql: str):
        async with await psycopg.AsyncConnection.connect(
                self.connection_string) as con:
            res = await con.execute(sql)
            try:
                columns = [i[0] for i in res.description]
                columns = [tuple(columns)]
                res = await res.fetchall()
                return columns + res
            except Exception:
                pass
            return None
