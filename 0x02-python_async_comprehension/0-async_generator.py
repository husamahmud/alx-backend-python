#!/usr/bin/env python3
"""
task 0
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    docs
    """
    random_max_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_max_delay)

    return random_max_delay
