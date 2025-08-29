# Manual entry for ranking items
import sys
import os
from sorter import interactive_rank

def read_items_manual():
	print("Enter your items one per line. Enter an empty line to finish:")
	items = []
	while True:
		item = input()
		if not item.strip():
			break
		items.append(item.strip())
	if not items:
		print("No items provided. Exiting.")
		sys.exit(0)
	return items