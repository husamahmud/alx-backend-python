#!/usr/bin/env python3
"""
task 9
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
	"""
	fixing its type annotation
	"""
	return [(i, len(i)) for i in lst]
