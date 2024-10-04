def countvowels(word: str) -> int:
    count = 0
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOU':
            count += 1
    return count

if __name__ == '__main__':
    assert countvowels('hello WORLD') == 3
    assert countvowels('crypt') == 0
