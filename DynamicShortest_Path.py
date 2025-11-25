import math

# DEFINE TRAVEL TIME FUNCTIONS
def T13(t):
    return 10

def T12(t):
    return 2 + t

def T34(t):
    return 5

def T24(t):
    return 2 + t

def T23(t):
    return max(8 - t / 2, 1)

# NETWORK STRUCTURE: DICT OF LINKS { (FROM, TO): FUNCTION }
links = {
    (1, 3): T13,
    (1, 2): T12,
    (3, 4): T34,
    (2, 4): T24,
    (2, 3): T23
}

# FUNCTION TO CHECK FIFO FOR A LINK
def check_fifo(link_func, link_name):
    # FOR DIFFERENTIABLE, CHECK T'(T) > -1
    t_values = [i for i in range(0, 101)]  # T FROM 0 TO 100
    arrival_times = [t + link_func(t) for t in t_values]
    is_increasing = all(arrival_times[i] < arrival_times[i+1] for i in range(len(arrival_times)-1))
    if is_increasing:
        return "SATISFIED"
    else:
        return "NOT SATISFIED"

# FUNCTION TO CALCULATE TOTAL TRAVEL TIME FOR A PATH
def total_travel_time(path, departure_time):
    current_time = departure_time
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i+1]
        link_func = links[(from_node, to_node)]
        travel_time = link_func(current_time)
        current_time += travel_time
    return current_time - departure_time

# POSSIBLE PATHS FROM 1 TO 4
paths = [
    [1, 2, 4],
    [1, 3, 4],
    [1, 2, 3, 4]
]

# PART (A): FIFO VERIFICATION
print("## PART (A): FIFO PRINCIPLE VERIFICATION")
for (from_node, to_node), func in links.items():
    status = check_fifo(func, f"{from_node}->{to_node}")
    print(f"* Link {from_node}->{to_node}: FIFO: {status}.")
print("CONCLUSION: THE FIFO PRINCIPLE IS SATISFIED FOR ALL LINKS IN THE NETWORK.\n")

# PART (B): SHORTEST PATHS
print("## PART (B): SHORTEST PATHS FROM NODE 1 TO NODE 4")
departure_times = [0, 2, 10]
for t in departure_times:
    print(f"* DEPARTURE TIME t={t}:")
    path_times = []
    for path in paths:
        tt = total_travel_time(path, t)
        path_times.append((path, tt))
        print(f"    - Path {path}: Travel Time = {tt}.")
    # FIND SHORTEST
    shortest = min(path_times, key=lambda x: x[1])
    print(f"    - SHORTEST PATH: {shortest[0]} WITH TRAVEL TIME = {shortest[1]}.\n")

# PART (C): PATH TRAVEL TIME EQUALITY
print("## PART (C): PATH TRAVEL TIME EQUALITY")
print("Path A: [1, 2, 4] Total Time T_A(t) = 3t + 6")
print("Path B: [1, 3, 4] Total Time T_B(t) = 15")
print("SETTING T_A(t) = T_B(t): 3t + 6 = 15")
print("SOLVING FOR t: t = 3")
print("THE TRAVEL TIMES ON PATHS [1, 2, 4] AND [1, 3, 4] ARE EQUAL FOR A DEPARTURE TIME OF t = 3.")