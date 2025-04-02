# Input: [9, 4, 9, 6, 7, 4]
# Output: (9,4)

#from collections import Counter

def get_repetead_number(array):

    count_map = {}
    repeated_number_set = set()

    for number in array:
        if number not in count_map:
            count_map[number] = 1
        else:
            count_map[number] += 1
    
    for number in array:
        if count_map[number] > 1:
            repeated_number_set.add(number)
    return repeated_number_set

# def get_repetead_number(nums):
#     count = Counter(nums)
#     for num in nums:
#         if count[num] > 1:
#        repeated_number_set.add(number)
#     return repeated_number_set

def main():
    test_list = [9, 4, 9, 6, 7, 4]
    print(get_repetead_number(test_list))

    
if __name__ == "__main__":
    main()