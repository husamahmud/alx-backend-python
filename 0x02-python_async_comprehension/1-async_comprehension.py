#!/usr/bin/env python3
"""
task 1
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
	"""
	docs
	"""
	output = []
	async for value in async_generator():
		output.append(value)

	return output
