import time #to track the time 
import tracemalloc #to track
import sys


# starting the monitoring memory usage
tracemalloc.start()
 
# record start time
start = time.time()

#setting to avoid python restriction errors
sys.set_int_max_str_digits(100000000)

#ITERATIVE FUNCTION
def factorial(n):
    i = 1
    for num in range(2, n + 1):
        i *= num
    return i

number = 5000000
print(number,"! =", factorial(number))

# record end time
end = time.time()
 
#setting to keep tract of the memory usage
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

# print the difference between start and end time (formula to get the run time) and converting to milliseconds
print("Iterative time : ",(end-start) * 10**3,"ms")

# memory usage display
stat = top_stats[0]
print("Iterative memory Usage : " "%s memory blocks - %.6f KiB" % (stat.count, stat.size / 1024))


# # Another way of displaying the memory : 
# for stat in snapshot.statistics("lineno"):
#     print(stat)

# stopping the monitoring of memory usage
tracemalloc.stop()

