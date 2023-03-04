#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tabulate import tabulate
#import tabulate function from tabulate module
def round_robin(n,processes, quantum):# creating function with 3 arguments
    """here n represents no.of processes ,quantum represents time quantum,processes is a list of tuples
    representing arrival time, burst time, and process name"""

    # initializing 3 lists of length n
    wait_time = [0] * n         # stores waiting time
    turnaround_time = [0] * n   # stores turn around time
    remaining_time = [0] * n    # stores remaining burst time
    for i in range(n):          # this loop initialize burst time to remaining_time
        remaining_time[i] = processes[i][1]  # here processes[i][1]=burst time
    t = 0                        # initialize current time
    completed = 0                # initialize complete to no.of processes completed
    #main loop for round_robin function
    while True:  # it continues until all the processes have completed execution
        done = True # sets to true
        for i in range(n):
            if processes[i][0] <= t and remaining_time[i] > 0: #comparing current time and remaining time
                 # iterate over all processes
                done = False     # sets to False
                if remaining_time[i] > quantum:
                    # If the remaining burst time for the process is greater than the time quantum,
                    # the algorithm subtracts the time quantum from the remaining burst time and adds the time quantum to t.
                    t += quantum
                    remaining_time[i] -= quantum
                else: # If the remaining burst time for the process is less than or equal to the time quantum,
                    t += remaining_time[i]
                    wait_time[i] = t - processes[i][0] - processes[i][1]
                    remaining_time[i] = 0
                    completed += 1
                    turnaround_time[i] = t - processes[i][0]
        if done == True:
            break
        if completed == n:
            break
    # calculating averages of waiting_time and turnaround time
    avg_wait_time = sum(wait_time) / n
    avg_turnaround_time = sum(turnaround_time) / n



    # Print the results in a table format
    results = []
    for i in range(n):
        process_name = processes[i][2]
        arrival_time = processes[i][0]
        burst_time = processes[i][1]
        turnaround = turnaround_time[i]
        waiting = wait_time[i]
        results.append([process_name,arrival_time, burst_time, turnaround, waiting])
    print(tabulate(results, headers=["Process", "Arrival Time", "Burst Time", "Turnaround Time", "Waiting Time"])) # tabulate function from tabulate mmodule

    print("Average waiting time:", avg_wait_time)
    print("Average turnaround time:", avg_turnaround_time)


n = int(input("Enter the number of processes: "))  # taking user input of no.of processes
quantum = int(input("Enter time quantum: "))       # taking user input of time quantum
processes = []                                     # create empty list
for i in range(n):                                 #iterating for loop n times=no.of processes
    arrival_time = int(input("Enter arrival time for process {}: ".format(i+1))) # taking user input of arrival time
    burst_time = int(input("Enter burst time for process {}: ".format(i+1)))# taking user input of burst time
    process_name = "P{}".format(i+1)
    processes.append([arrival_time, burst_time, process_name]) # apppending all to process list  with inner tuples inside

round_robin(n,processes, quantum)


# In[ ]:





# In[ ]:




