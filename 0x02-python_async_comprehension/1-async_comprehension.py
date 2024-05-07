#!/usr/bin/env python3
"""
task 1
"""


import typing
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    docs
    """
    upcoming = []
    for _ in range(n):
        upcoming.append(wait_random(max_delay))

    output = []
    for u in asyncio.as_completed(upcoming):
        output.append(await u)

    return output
