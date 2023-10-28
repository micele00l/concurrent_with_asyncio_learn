import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial, reduce
import time
from typing import Dict, List
from chp6.code68 import partition, merge_dictionaries, map_frequencies


async def reduce(counters, chunk_size: int):
    chunks: List[List[Dict]] = list(partition(counters, chunk_size))
    reducers = []
    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = partial(reduce, merge_dictionaries, chunk)

        reducer_chunks =await asyncio.gather(*reducers) 
        chunks =list(partition(reducer_chunks, chunk_size))
        reducers.clear()
    return chunks[0][0]

# unfinish
# have not finish read book 