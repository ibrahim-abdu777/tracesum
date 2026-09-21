"""Summarize level= fields in newline-delimited trace logs."""
from collections import Counter


def summarize(lines):
    counts = Counter()
    for line in lines:
        for token in line.split():
            if token.startswith("level="):
                counts[token[len("level="):]] += 1
    return dict(counts)


def summarize_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return summarize(handle)
