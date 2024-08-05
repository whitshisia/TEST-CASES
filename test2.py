# def solution(R, V):
#     current_balance_A = 0
#     current_balance_B = 0
#     min_initial_A = 0
#     min_initial_B = 0
    
#     for i in range(len(R)):
#         if R[i] == "A":
#             current_balance_B += V[i]  # B receives money
#             current_balance_A -= V[i]  # A loses money
#             if current_balance_A < 0:
#                 min_initial_A = max(min_initial_A, -current_balance_A)
#         elif R[i] == "B":
#             current_balance_A += V[i]  # A receives money
#             current_balance_B -= V[i]  # B loses money
#             if current_balance_B < 0:
#                 min_initial_B = max(min_initial_B, -current_balance_B)
    
#     return [min_initial_A, min_initial_B]

# # Examples
# print(solution("BAABA", [2, 4, 1, 1, 2]))  # Expected output: [2, 4]
# print(solution("ABAB", [10, 5, 10, 15]))  # Expected output: [0, 15]
# print(solution("B", [100]))               # Expected output: [100, 0]

def solution(P, Q):
    # Create a set to store the distinct letters in P and Q
    distinct_letters = set(P + Q)
    
    # Initialize the minimum number of distinct letters to the total number of distinct letters
    min_distinct_letters = len(distinct_letters)
    
    # Iterate over each distinct letter
    for letter in distinct_letters:
        # Initialize a set to store the letters in the current string S
        curr_distinct_letters = set()
        
        # Initialize a flag to indicate if the current letter can be chosen for all positions
        can_choose_all = True
        
        # Iterate over each position in the strings
        for p, q in zip(P, Q):
            # If the current letter is not in the current position, choose the letter that is not in the current string S
            if letter not in (p, q):
                if p not in curr_distinct_letters:
                    curr_distinct_letters.add(p)
                else:
                    curr_distinct_letters.add(q)
                    can_choose_all = False
            # If the current letter is in the current position, add it to the current string S
            else:
                curr_distinct_letters.add(letter)
        
        # If the current letter can be chosen for all positions, update the minimum number of distinct letters
        if can_choose_all:
            min_distinct_letters = min(min_distinct_letters, len(curr_distinct_letters))
    
    return min_distinct_letters
print (solution("axxz", "yzwy"))