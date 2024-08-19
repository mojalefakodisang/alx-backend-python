#!/usr/bin/env python3
"""Module that contains an asynchronous function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    values = []
    for x in range(n):
        values.append(await wait_random(max_delay))

    for n in range(len(values)):
        for m in range(0, len(values) - n - 1):
            if values[m] > values[m + 1]:
                values[m], values[m + 1] = values[m + 1], values[m]

    return values
