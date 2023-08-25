import asyncpg
import asyncio

product_query = \
    """
SELECT
p.product_id,
p.product_name,
p.brand_id,
s.sku_id,
pc.product_color_name,
ps.product_size_name
FROM product AS p
JOIN sku AS s ON s.product_id = p.product_id
JOIN product_color AS pc ON pc.product_color_id = s.product_color_id
JOIN product_size AS ps ON ps.product_size_id = s.product_size_id
WHERE p.product_id = 100"""


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def main():
    async with asyncpg.create_pool(host='test.local',
                                   port=5432,
                                   user='postgres',
                                   database='products',
                                   password='password',
                                   min_size=6,
                                   max_size=6) as pool:

        await asyncio.gather(query_product(pool),
                             query_product(pool))
