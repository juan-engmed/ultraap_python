# Input: [9, 4, 9, 6, 7, 4]
# Output: 6  # 6 é o primeiro não repetido, no índice 3

#from collections import Counter

def first_non_repeated(array):

    count_map = {}
    for number in array:
        if number not in count_map:
            count_map[number] = 1
        else:
            count_map[number] += 1
    
    for number in array:
        if count_map[number] == 1:
            return number

# def first_non_repeated(nums):
#     count = Counter(nums)
#     for num in nums:
#         if count[num] == 1:
#             return num
#     return None

def main():
    test_list = [9, 4, 9, 6, 7, 4]
    print(first_non_repeated(test_list))

    
if __name__ == "__main__":
    main()