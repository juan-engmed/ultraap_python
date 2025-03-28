def find_min_index(array):
    minor_item = array[0]
    minor_index = 0
    
    for i in range(1, len(array)):
        item = array[i]
        if array[i] < minor_item:
            minor_item = item
            minor_index = i
    return minor_index

def selection_sort(array):
    merge_array = []

    for i in range(len(array)): #O(n)
        minor_index_for_minor_element = find_min_index(array) #O(n)
        minor_element = array[minor_index_for_minor_element]
        array.pop(minor_index_for_minor_element)
        merge_array.append(minor_element)
    
    return merge_array

#O(n²)

def main():
    merge_list = selection_sort([4, 3, 7, 9, 2])
    print(merge_list)


if __name__ == "__main__":
    main()