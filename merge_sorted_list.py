import heapq

def merge_sorted_lists(all_lists):
    merged_list = []
    heap = []
    
    # Add the first element of each list to the heap
    for i in range(len(all_lists)):
        if len(all_lists[i]) > 0:
            heapq.heappush(heap, (all_lists[i][0], i, 0))
    
    # While the heap is not empty, remove the smallest element and add it to the merged list
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        merged_list.append(val)
        
        # Add the next smallest element from the same list to the heap
        if element_idx < len(all_lists[list_idx]) - 1:
            heapq.heappush(heap, (all_lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
            
    return merged_list
    
# Sample input
all_lists = [[2, 5, 9, 21], [-1, 0, 2], [-10, 81, 121], [4, 6, 12, 20, 150]]

# Output
print(merge_sorted_lists(all_lists))
