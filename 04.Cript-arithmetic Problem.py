import itertools

def solve_cryptarithm(words, result):
    unique_letters = set(''.join(words) + result)
    if len(unique_letters) > 10:
        return "Too many unique letters for a solution."

    letters = ''.join(unique_letters)
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue

        words_values = [sum(mapping[char] * (10 ** idx) for idx, char in enumerate(word[::-1])) for word in words]
        result_value = sum(mapping[char] * (10 ** idx) for idx, char in enumerate(result[::-1]))

        if sum(words_values) == result_value:
            solution = {char: mapping[char] for char in letters}
            return f"Solution found: {solution}"

    return "No solution found."

words = input("Enter the words (separated by spaces): ").upper().split()
result = input("Enter the result word: ").upper()

print(solve_cryptarithm(words, result))
