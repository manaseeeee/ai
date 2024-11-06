from itertools import permutations

def is_valid_solution(word1, word2, word3, solution):
    # Convert words to numbers using the solution mapping
    num1 = int(''.join([str(solution[letter]) for letter in word1]))
    num2 = int(''.join([str(solution[letter]) for letter in word2]))
    num3 = int(''.join([str(solution[letter]) for letter in word3]))
    
    # Check if the equation holds
    return num1 + num2 == num3

def cryptarithmetic():
    # Define the words in the cryptarithmetic equation
    word1 = "SEND"
    word2 = "MORE"
    word3 = "MONEY"
    
    # Get unique letters in the equation
    letters = set(word1 + word2 + word3)
    
    # We need to make sure we have exactly 10 unique letters, because we have 10 digits (0-9)
    if len(letters) > 10:
        raise ValueError("Too many unique letters, cannot be solved with 10 digits.")
    
    # Generate all possible permutations of the digits 0-9
    for perm in permutations(range(10), len(letters)):
        # Create a mapping of letters to digits
        solution = dict(zip(letters, perm))
        
        # Check if the solution satisfies the equation
        if is_valid_solution(word1, word2, word3, solution):
            return solution
    
    return None

# Find the solution
solution = cryptarithmetic()

if solution:
    print("Solution found!")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
