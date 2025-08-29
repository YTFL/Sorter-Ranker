import os
import re
from sorter import interactive_rank

def is_valid_item(item):
	# Accept names with punctuation, apostrophes, dots, etc.
	item = item.strip()
	if not item:
		return False
	# Heuristic: reject if item is a full sentence (ends with . ! ? and has more than 6 words)
	if len(item.split()) > 6 and re.search(r'[.!?]$', item):
		return False
	# Reject if item contains multiple sentence-ending punctuations (likely a sentence)
	if len(re.findall(r'[!?]', item)) >= 1 or len(re.findall(r'[.]', item)) > 3:
		return False
	return True

def read_items_from_txt(file_path):
	if not os.path.isfile(file_path):
		raise FileNotFoundError(f"File not found: {file_path}")
	with open(file_path, 'r', encoding='utf-8') as f:
		content = f.read()
	# Split by newlines and commas
	raw_items = []
	for line in content.splitlines():
		for part in line.split(','):
			part = part.strip()
			if part:
				raw_items.append(part)
	# Only check the first item for validity
	if not raw_items or not is_valid_item(raw_items[0]):
		raise ValueError("Text file rejected: first item is not a valid name.")
	items = [item for item in raw_items if item.strip()]
	return items