def find_anagrams(word, candidates):
    return [
        x
        for x in candidates
        if x.casefold() != word.casefold()
        and sorted(x.casefold()) == sorted(word.casefold())
    ]
