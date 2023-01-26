print("***************PROGRAMMED BY******************")
print("**********Kevin Joseph G. Concepcion**********")
print("*****************BSCOE 2-2********************")


def bubble_sort(unique_values):
    for i in range(len(unique_values)-1,0,-1):
        for j in range(i):
            if unique_values[j] > unique_values[j+1]:
                temp = unique_values[j]
                unique_values[j] = unique_values[j+1]
                unique_values[j+1] = temp


unique_values = [57, 26, 28, 88, 55, 78, 90, 79, 27, 35]