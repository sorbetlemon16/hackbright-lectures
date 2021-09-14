"""This merge sort is written for ease of understanding. An implementation
with better runtime is implemented in sorts.py."""


def merge_sort(lst):
    """Merge sort list and return result."""

    print("calling merge_sort on", lst)

    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        print("returning", lst)
        return lst

    mid = int(len(lst) / 2)  # index at half the list
    lst1 = merge_sort(lst[:mid])  # divide list in half
    print("list 1 done")
    lst2 = merge_sort(lst[mid:])  # assign other half

    return make_merge(lst1, lst2)


def make_merge(lst1, lst2):
    """Merge lists."""

    # Compare first items of each pair of lists & interleave
    result_list = []
    print(lst1, lst2)
    while len(lst1) > 0 or len(lst2) > 0:
        # if items left in both lists
        # compare first items of each list
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            # append and rm first item of lst1
            result_list.append(lst1.pop(0))
        else:
            # append and rm first item of lst2
            result_list.append(lst2.pop(0))

    print("returning merge", result_list)
    return result_list


if __name__ == "__main__":
    print(merge_sort([2, 1, 7, 4]))
