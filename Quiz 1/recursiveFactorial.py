import time #to track the time 
import tracemalloc #to track
import sys #to set some settings to avoid default errors 


# starting the monitoring memory usage
tracemalloc.start()
 
# record start time
start = time.time()

#setting to avoid python restriction errors
sys.setrecursionlimit(100000000)
sys.set_int_max_str_digits(100000000)

#RECURSIVE FUNCTION
def factorial(n):
    if n==1 : #base case
        return n
    else:
        return n * factorial(n-1) #recursive case

number = 4000
print(number, "! =", factorial(number))

# record end time
end = time.time()
 
#setting to keep tract of the memory usage
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

# print the difference between start and end time (formula to get the run time) and converting to milliseconds
print("Recursive time : ",(end-start) * 10**3,"ms")

# memory usage display
stat = top_stats[0]
print("Recursive memory Usage : " "%s memory blocks - %.6f KiB" % (stat.count, stat.size / 1024))


# # Another way of displaying the memory : 
# for stat in snapshot.statistics("lineno"):
#     print(stat)

# stopping the library
tracemalloc.stop()


