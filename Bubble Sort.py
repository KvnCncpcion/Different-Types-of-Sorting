print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")

print("Using Bubble Sort")
print("\nThis should be the elements contained in the array: [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]")

def bubble_sort(unique_values):
    for i in range(len(unique_values)-1,0,-1):
        for j in range(i):
            if unique_values[j] > unique_values[j+1]:
                temp = unique_values[j]
                unique_values[j] = unique_values[j+1]
                unique_values[j+1] = temp


unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]
bubble_sort(unique_values)
print("\nThis is the result in using the Bubble Sort function:",unique_values)

# Reference for the code: https://www.youtube.com/watch?v=Vca808JTbI8