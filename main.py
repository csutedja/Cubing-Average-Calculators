time1 = input("Enter 5 solve times, seperating each time by hitting enter." + "\n")
time2 = input("")
time3 = input("")
time4 = input("")
time5 = input("")


time_list = [time1, time2, time3, time4, time5]

sum_of_times = sum([float(x) for x in time_list])


maxnum = 0
minnum = 0

def find_min_num(list): # function to determine fastest time 
  minnum = list[0]
  for x in time_list:
    if x < minnum:
      minnum = x
  return minnum

def find_max_num(list): # function to determine slowest time
  maxnum = list[0]
  for x in time_list:
    if x > maxnum:
      maxnum = x
  return maxnum
minnum = find_min_num(time_list)
maxnum = find_max_num(time_list)
three_solves = float(sum_of_times) - float(minnum) - float(maxnum) 
ao5 = three_solves/3
print("Your average of 5 is: " + str(ao5))
