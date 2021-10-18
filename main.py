import sorting.sorting as s
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# configuring runtime parameters
if __name__ == "__main__":
    N = int(input("Enter the number of integers to sort: "))
    method_msg = "Enter sorting method:\n(b)ubble\n(i)nsertion\n(q)uick\n(s)election\n"
    method = input(method_msg)

    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)
    

    if method =="b":
        title = "Bubble Sort"
        generator = s.bubble_sort(A)
    elif method == "i":
        title = "Insertion Sort"
        generator = s.insertion_sort(A)
    elif method == "s":
        title = "Selection Sort"
        generator = s.selection_sort(A)
    elif method == "q":
        title = "Quick Sort"
        generator = s.quick_sort(A, 0, len(A) - 1)
    

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)), A, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07*N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # defining the animation
    iteration = [0]
    def fig_update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))
    
    anim = FuncAnimation(fig, func=fig_update, fargs=(bar_rects, iteration), frames=generator, interval=1, repeat=False)
    plt.show()