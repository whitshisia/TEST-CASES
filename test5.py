# from datetime import datetime

# def StringChallenge(strArr):
#     # _define-ocg_ Convert time strings to minutes since midnight
#     def convert_to_minutes(time_str):
#         return int(datetime.strptime(time_str, "%I:%M%p").strftime("%H")) * 60 + int(datetime.strptime(time_str, "%I:%M%p").strftime("%M"))
    
#     # Convert all time strings in strArr to minutes since midnight
#     times_in_minutes = [convert_to_minutes(time) for time in strArr]
    
#     # Sort the list of times (in minutes)
#     times_in_minutes.sort()
    
#     # Initialize the smallest difference to a large value
#     smallest_diff = float('inf')
    
#     # Calculate the differences between consecutive times in the sorted list
#     for i in range(1, len(times_in_minutes)):
#         diff = times_in_minutes[i] - times_in_minutes[i-1]
#         smallest_diff = min(smallest_diff, diff)
    
#     # Check the difference between the last and first time across midnight
#     midnight_diff = 1440 + times_in_minutes[0] - times_in_minutes[-1]
#     smallest_diff = min(smallest_diff, midnight_diff)
    
#     return smallest_diff

# # Example usage:
# print(StringChallenge(["1:10pm", "4:40am", "5:00pm"]))  # Output: 230
# print(StringChallenge(["10:00am", "11:45pm", "5:00am", "12:01am"]))  # Output: 16

# # _define-ocg_ We directly work with the list of time differences in minutes

import re

def StringChallenge(str):
    # _define-ocg_ This function checks if a word contains exactly 3 unique, non-adjacent digits
    def has_three_unique_non_adjacent_digits(word):
        # Extract all digits from the word
        digits = re.findall(r'\d', word)
        
        # Check if there are exactly 3 unique digits
        unique_digits = set(digits)
        if len(unique_digits) != 3:
            return False
        
        # Check adjacency by ensuring no three consecutive characters are all digits
        for i in range(len(word) - 2):
            if word[i].isdigit() and word[i+1].isdigit() and word[i+2].isdigit():
                return False
        
        return True
    
    # Split the input string into words and check each word
    words = str.split()
    for word in words:
        if not has_three_unique_non_adjacent_digits(word):
            return "false"
    
    return "true"

# Example usage:
print(StringChallenge("2a3b5 w1o2rl3d g1gg92"))  # Output: true
print(StringChallenge("21aa3a ggg4g4g6ggg"))      # Output: false

# _define-ocg_ The function directly checks digit adjacency within each word