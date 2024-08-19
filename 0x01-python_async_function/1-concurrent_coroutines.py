#!/usr/bin/env python3
"""Module that contains an asynchronous function"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function"""
    coroutines = []
    for i in range(n):
        coroutines.append(wait_random(max_delay))
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
