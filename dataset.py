from typing import List, Tuple

def build_skipgram_pairs(tokens: List[int], context_window: int) -> List[Tuple[int, int]]:
    pairs: List[Tuple[int, int]] = []
    n = len(tokens)

    for i, center in enumerate(tokens):

        start = max(0, i - context_window)
        end = min(n, i + context_window + 1)

        for j in range(start, end):
            if j == i:
                continue

            context = tokens[j]
            pairs.append((center, context))

    return pairs