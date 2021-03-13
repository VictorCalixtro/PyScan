import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PyScan as p
import sys

def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("Number of Operations: {}".format(iteration[0]))


message = "Welcome to PyScan"
print(message)
print("Enter an integer: ")
size = int(input("Number: "))

chooseAlgorithm = """Select your algorithm
        1. Bubble Sort
        2. Insertion Sort
        3. Merge Sort
        4. Quick Sort
        5. Selection Sort
        6. Quit"""

print(chooseAlgorithm)
choice = "Choice: "
method = input(choice)
numberList = [x + 1 for x in range(size)]
random.seed(time.time())
random.shuffle(numberList)

        
if method == "1":
    title = "QuickSort Algorithm"
    generator = p.quicksort(numberList, 0, size - 1)
elif method == "2":
    title = "SelectionSort Algorithm"
    generator = p.selectionsort(numberList)
elif method == "3":
    title = "MergeSort Algorithm"
    generator = p.mergesort(numberList, 0, size - 1)
elif method == "4":
    title = "BubbleSort Algorithm"
    generator = p.bubblesort(numberList)
elif method == '5':
    title = "InsertionSort Algorithm"
    generator = p.insertionsort(numberList)
else:
    print("Exiting the program...")
    sys.exit()
    
fig, ax = plt.subplots()
ax.set_title(title)
    
    
bar_rects = ax.bar(range(len(numberList)), numberList, align="edge", color="r", alpha=0.5)
ax.set_xlim(0, size)
ax.set_ylim(0, int(1.07 * size))
text = ax.text(0.03, 0.97, "", transform=ax.transAxes)
iteration = [0]

anim = animation.FuncAnimation(fig, func=update_fig,
fargs=(bar_rects, iteration), frames=generator, interval=1,
repeat=False)
plt.show()
    