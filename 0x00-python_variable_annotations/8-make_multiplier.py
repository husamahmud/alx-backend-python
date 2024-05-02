#!/usr/bin/env python3
"""
task 8
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
	"""
	takes a float and return it multiblied by multiblier
	"""
	return lambda x: x * multiplier
