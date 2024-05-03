#!/usr/bin/env python3
"""
task 100
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
	"""
	fixing its type annotation
	"""
	if lst:
		return lst[0]
	else:
		return None
