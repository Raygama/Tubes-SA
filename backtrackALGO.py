import time

def climbingStairs(i, n):
    if i > n:
        return 0
    if i == n:
        return 1
    
    return climbingStairs(i + 1, n) + climbingStairs(i + 2, n)

def countClimbingStairs(n):
    return climbingStairs(0, n)

n = 40

start_time = time.time_ns()
cara = countClimbingStairs(n)
end_time = time.time_ns()

run_time = end_time - start_time

print(f"Number of ways to climb {n} adalah: {cara}")
print(f"Run time: {run_time:.20f} nanoseconds")
