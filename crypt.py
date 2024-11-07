from itertools import permutations

def is_valid_solution(word1, word2, word3, solution):
    num1 = int(''.join([str(solution[letter]) for letter in word1]))
    num2 = int(''.join([str(solution[letter]) for letter in word2]))
    num3 = int(''.join([str(solution[letter]) for letter in word3]))
    return num1 + num2 == num3

def cryptarithmetic():
    word1 = "SEND"
    word2 = "MORE"
    word3 = "MONEY"
    letters = set(word1 + word2 + word3)
    
    if len(letters) > 10:
        raise ValueError("Too many unique letters, cannot be solved with 10 digits.")
    
    for perm in permutations(range(10), len(letters)):
        solution = dict(zip(letters, perm))
        if is_valid_solution(word1, word2, word3, solution):
            return solution
    
    return None

solution = cryptarithmetic()

if solution:
    print("Solution found!")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
