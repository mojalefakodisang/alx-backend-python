#!/usr/bin/env python3
"""Module containing async function"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async function returning numbers from Async generator"""
    return [i async for i in async_generator()]
