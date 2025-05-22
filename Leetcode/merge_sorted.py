

def merge_sorted_lists(list1, list2):
    i = j = 0
    merged_list = []

    # Enquanto houver elementos em ambas as listas
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Adiciona os elementos restantes de list1 (se houver)
    #merged_list.extend(list1[i:])
    
    # Adiciona manualmente os elementos restantes de list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Adiciona os elementos restantes de list1 (se houver)
    #merged_list.extend(list2[j:])
    
    # Adiciona manualmente os elementos restantes de list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

print(merge_sorted_lists([0,3,4,31], [4,6,30]))