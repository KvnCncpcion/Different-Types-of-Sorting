print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")

print("Using Insertion Sort")
print("\nThis should be the elements contained in the array: [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]")

def insertion_sort(unique_values):
    for i in range(1, len(unique_values)):
        j = i
        while unique_values[j - 1] > unique_values[j] and j > 0:
            unique_values[j - 1], unique_values[j] = unique_values[j], unique_values[j - 1]
            j -= 1


unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]
insertion_sort(unique_values)
print("\nThis is the result in using the Insertion Sort function:",unique_values)

# Reference for the code: https://www.youtube.com/watch?v=R_wDA-PmGE4