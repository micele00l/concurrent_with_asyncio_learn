import asyncpg


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


async def main():
    connection = await asyncpg.connect(host='test.local',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')

    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM produc'
        products_generator = connection.cursor(query)
        async for product in take(products_generator, 5):
            print(product)
        print('got the first products')

    await connection.close()
