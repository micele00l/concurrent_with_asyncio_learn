import asyncpg
from typing import List, Tuple, Union
from random import sample


def load_common_words() -> List[str]:
    with open('common_words.txt') as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, str]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands_str = 'INSERT INTO brand VALUES(DEFAULT, $1)'
    return await connection.executemany(insert_brands_str, brands)


async def main():
    connection = await asyncpg.connect(host='test.local',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')
    common_words = load_common_words()
    await insert_brands(common_words, connection)
