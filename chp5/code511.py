import asyncpg
import logging


async def main():
    connection = await asyncpg.connect(host='test.local',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')

    async with connection.transaction():
        insert_brand = "INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')"
        await connection.execute(insert_brand)
        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1,'black')")
        except Exception as ex:
            logging.warning(
                'Ignoring error inserting product color', exc_info=ex)

    await connection.close()
