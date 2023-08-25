import asyncpg


async def main():
    connection = await asyncpg.connect(host='test.local',
                                       port=5432,
                                       user='postgres',
                                       database='postgres',
                                       password='password')
    version = connection.get_server_version()
    print(f'Connected! Postgres version is {version}')
    await connection.close() 
