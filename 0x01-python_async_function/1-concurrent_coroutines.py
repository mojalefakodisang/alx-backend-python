#!/usr/bin/env python3
"""Module that contains an asynchronous function"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """Asynchronous function"""
    values = []
    for i in range(n):
        values.append(wait_random(max_delay))
    delays = await asyncio.gather(*values)
    return sorted(delays)
