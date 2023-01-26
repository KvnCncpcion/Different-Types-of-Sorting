print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")

def quick_sort(unique_values, left, right):
    if left < right:
        partition_pos = partition(unique_values, left, right)
        quick_sort(unique_values, left, partition_pos - 1)
        quick_sort(unique_values, partition_pos + 1, right)

def partition(unique_values, left, right):
    i = left
    j = right - 1
    pivot = unique_values[right]

    while i < j:
        while i < right and unique_values[i] < pivot:
            i += 1
        while j > left and unique_values[j] >= pivot:
            j -= 1

        if i < j:
            unique_values[i], unique_values[j] = unique_values[j], unique_values[i]

    if unique_values[i] > pivot:
        unique_values[i], unique_values[right] = unique_values[right], unique_values[i]

    return i

unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]
quick_sort(unique_values, 0, len(unique_values) - 1)
print("This is the result in using the Quick So",unique_values)