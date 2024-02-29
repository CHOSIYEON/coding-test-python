def solution(citations):
    citations = sorted(citations, reverse=True)

    for idx, value in enumerate(citations):
        if idx >= value:
            return idx

    return len(citations)