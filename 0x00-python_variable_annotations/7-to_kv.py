#!/usr/bin/env python3
"""
task 7
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
	"""
	takes a string k and an int OR float v as arguments and returns a tuple
	"""
	return k, v ** 2
