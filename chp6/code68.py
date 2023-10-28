import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial, reduce
import time
from typing import List, Dict


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] += int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] += second[key]
        else:
            merged[key] = second[key]
    return merged


async def main(partition_size: int):
    filename = 'googlebooks-eng-all-1gram-20120701-a'
    with open(filename, encoding='utf-8') as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(
                    pool, partial(map_frequencies, chunk)))

            intermediate_results = await asyncio.gather(*tasks)
            final_result = reduce(merge_dictionaries, intermediate_results)
            print(f'aardvark has appeared {final_result["Aardvark"]} times')

            end = time.time()
            print(f'MapReduce took: {(end-start):.4f} second(s)')

if __name__ == '__main__':
    asyncio.run(main(60000))
