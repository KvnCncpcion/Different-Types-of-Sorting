print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")

def merge_sort(unique_values):
    if len(unique_values) > 1:
        left_array = unique_values[:len(unique_values)//2]
        right_array = unique_values[len(unique_values)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                unique_values[k] = left_array[i]
                i += 1
                k += 1
            else:
                unique_values[k] = right_array[j]
                j += 1
                k += 1

        while i < len(left_array):
            unique_values[k] = left_array[i]
            i += 1
            k += 1
            
        while j < len(right_array):
            unique_values[k] = right_array[j]
            j += 1
            k += 1

unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]