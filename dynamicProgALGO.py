import time
def climbingStairs(n):
    if n == 0:
        return 0
    stair = [0] * (n + 1)
    stair[0] = 0
    stair[1] = 1
    stair[2] = 2
    for i in range(3, n+1):
        stair[i] = stair[i-1] + stair[i-2]

    return stair[n]

n = 1000000
start_time = time.time_ns()
cara = climbingStairs(n)
end_time = time.time_ns()

run_time = end_time - start_time

print(f"Number of ways to climb {n} adalah: {cara}")
print(f"Run time: {run_time:.20f} nanoseconds")