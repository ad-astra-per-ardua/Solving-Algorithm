// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from collections import deque

def can_change(cur_word, words):
    can_change_words = []
    for word in words:
        diff_count = 0
        for a, b in zip(cur_word, word):
            if a != b:
                diff_count += 1
        if diff_count == 1:
            can_change_words.append(word)
    return can_change_words

def solution(begin, target, words):
    visited = []
    que = deque([(begin, 0)])

    while que:
        cur_word, cur_count = que.popleft()

        if cur_word == target:
            return cur_count

        for word in can_change(cur_word, words):
            if word not in visited:
                que.append((word, cur_count + 1))
                visited.append(word)

    return 0
