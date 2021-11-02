import sorting.algorithms as sa
import random
import time
import sys
import pygame

dimensions = (1024, 512)

# list all of the different sorting algorithms
algorithms = {"BubbleSort": sa.BubbleSort(), \
              "InsertionSort": sa.InsertionSort(), \
              "QuickSort": sa.QuickSort(), \
              "SelectionSort": sa.SelectionSort()}

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        print("")
        sys.exit(0)

pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("black"))

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()

def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("black"))
    k = int(dimensions[0]/len(algorithm.array))

    for i in range(len(algorithm.array)):
        color = "white"
        if swap1 == algorithm.array[i]:
            color = "red"
        elif swap2 == algorithm.array[i]:
            color = "green"
        pygame.draw.rect(display, color, (i*k, dimensions[1] - algorithm.array[i], k, algorithm.array[i]))
    check_events()
    pygame.display.update()


def keep_open(algorithm, display, time):
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Enter a sorting algorithm.")
    else:
        try:
            algorithm = algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error")


if __name__ == "__main__":
    main()