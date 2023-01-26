print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")


def selection_sort(unique_values):
    for i in range(0, len(unique_values) - 1):
        cur_min_index = i
        for j in range(i + 1, len(unique_values)):
            if unique_values[j] < unique_values[cur_min_index]:
                cur_min_index = j

        unique_values[i], unique_values[cur_min_index] = unique_values[cur_min_index], unique_values[i]

unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]