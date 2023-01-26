print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")

def insertion_sort(unique_values):
    for i in range(1, len(unique_values)):
        j = 1
        while unique_values[j -1] > unique_values[j] and unique_values > 0:
            unique_values[j - 1], unique_values[j] = unique_values[j], unique_values[j - 1]
            j -= 1


unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]