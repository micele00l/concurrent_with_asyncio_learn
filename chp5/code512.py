import asyncpg
from asyncpg.transaction import Transaction


async def main():
    connection = await asyncpg.connect(host='test.local',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')

    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        insert_brand_1 = "INSERT INTO brand VALUES(DEFAULT, 'brand_1')"
        insert_brand_2 = "INSERT INTO brand VALUES(DEFAULT, 'brand_2')"
        await connection.execute(insert_brand_1)
        await connection.execute(insert_brand_2)
    except asyncpg.PostgresError:
        print('Errors, rolling back transaction!')
        await transaction.rollback()
    else:
        print('No errors, committing transaction!')
        await transaction.commit()

    query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()
