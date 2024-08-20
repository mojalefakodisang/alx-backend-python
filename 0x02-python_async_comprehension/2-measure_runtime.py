#!/usr/bin/env python3
"""Module containing async function"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return total runtime of four async functions parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
