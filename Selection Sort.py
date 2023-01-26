print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")

print("Using Selection Sort")
print("\nThis should be the elements contained in the array: [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]")

def selection_sort(unique_values):
    for i in range(0, len(unique_values) - 1):
        cur_min_index = i
        for j in range(i + 1, len(unique_values)):
            if unique_values[j] < unique_values[cur_min_index]:
                cur_min_index = j

        unique_values[i], unique_values[cur_min_index] = unique_values[cur_min_index], unique_values[i]

unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]
selection_sort(unique_values)
print("\nThis is the result in using the Selection Sort function:",unique_values)

# Reference for code: https://www.youtube.com/watch?v=ee80YmiaSVQ