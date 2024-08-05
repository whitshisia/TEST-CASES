# from itertools import permutations
# def solution(A,B,C,D):
#     list = [A,B,C,D]
#     time = set()
    
#     for x in permutations(list):
#         hr = str(x[0] ) + str(x[1])
#         mins = str(x[2]) + str(x[3])
        
#         if 0<= int(hr) <= 23 and int(mins) < 60:
#             time.add(int(hr) + ":" + int(mins))
            
#     return len(time)        

# def solution(skills):
#     n = len(skills)
#     results = [0] * n
#     players = list(range(n))
    
#     round_number = 1
    
#     while len(players) > 1:
#         next_round_players = []
#         for i in range(0, len(players), 2):
#             p1 = players[i]
#             p2 = players[i+1]
#             if skills[p1] > skills[p2]:
#                 next_round_players.append(p1)
#                 results[p2] = round_number
#             else:
#                 next_round_players.append(p2)
#                 results[p1] = round_number
#         players = next_round_players
#         round_number += 1
    
#     results[players[0]] = round_number - 1  # The winner's last round is the final round
#     return results

# # Examples
# print(solution([4, 2, 7, 3, 1, 8, 6, 5]))  # Expected output: [2, 1, 3, 1, 1, 3, 2, 1]
# print(solution([4, 2, 1, 3]))             # Expected output: [2, 1, 1, 2]
# print(solution([3, 4, 2, 1]))             # Expected output: [1, 2, 2, 1]

# def solution (S):
#     seen_b = False
#     for char in S:
#         if char == 'b' and not seen_b:
#             seen_b = True
#         elif char == 'a' and seen_b:
#             return False
#     return True
# print (solution("bbb"))

# def solution(N):
#     # Base lowercase alphabet
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
    
#     # Determine full repetitions and remainder
#     full_repeats = N // 26
#     remainder = N % 26
    
#     # Construct the base part of the string with full repetitions of the alphabet
#     result = alphabet * full_repeats
    
#     # Add the remaining characters to complete the string of length N
#     result += alphabet[:remainder]
    
#     return result

# # Example test cases
# print(solution(3))   # Possible outputs: "abc", "def", "ghi", etc.
# print(solution(5))   # Possible outputs: "abcde", "fghij", "klmno", etc.
# print(solution(30))  # Output: "abcdefghijklmnopqrstuvwxyzabcd" (each letter 'a' to 'o' appears once)

# # You can test with other values of N within the range [1..200,000]
# print(solution(52))  # Output: "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# print(solution(53))  # Output: "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza"
# print(solution(1))   # Output: "a"
# print(solution(200000))  # A long string with equal distribution of letters

def change(st):
    result = ['0'] * 26
    
    low = st.lower()
    for char in low:
        if 'a' <= char <= z:
            index = ord(char) - ord('a')
            result[index] = '1'
            
    return ''.join(result)        