def repeat(): # function that is called at the end of a calculation that asks user if they want to repeat
    question = str(input("\nWould you like to calculate another average?\n1) Type in 'y' or '1' to calculate a new average \n2) Type in 'n' or '2' to finish and exit this program "))
    if question == str(1) or question == str("y"):
      main()
    if question == str(2) or question == str("n"):
      print("\nThank you for using this program! If you have any issues be sure to put them in the project's GitHub program. ")
      raise SystemExit # any future instances of SystemExit, including this one, are used to end the program
    else:
      print("Invalid input! ")
      repeat()
def main(): # entire program, including all calculations, is done in here    
  time_list = [] # declaring a list variable 
  question = str(input("Which average would you like to calculate? \n1) Mean of 3 (mo3) \n2) Average of 5 (ao5) \n3) Average of 12 (ao12) \n4) Exit this program \n\n"))
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
  if question == str(1):
    sum_of_times = 0
    for i in range(0,3):
      try:
        time_input = float(input("\nPlease input a time in seconds, seperating each one with ENTER key "))
        time_list.append(time_input)
      except ValueError:
        print("\nInvalid input! ")
        repeat()
    sum_of_times = sum([float(x) for x in time_list])
    mean_of_three = sum_of_times / 3
    print("\nYour mean of 3 is " + str(round(mean_of_three, 2)) + " seconds.")
    repeat()
  
  elif question == str(2):
   sum_of_times = 0
   for i in range(0, 5):
      try:
        time_input = float(input("\nPlease input a time in seconds, seperating each one with ENTER key "))
        time_list.append(time_input)
      except ValueError:
        print("\nInvalid input! ")
        repeat()
   sum_of_times = sum([float(x) for x in time_list])  
   maxnum = 0
   minnum = 0
   minnum = find_min_num(time_list)
   maxnum = find_max_num(time_list)
   three_solves = float(sum_of_times) - float(minnum) - float(maxnum) 
   ao5 = three_solves/3
   print("\nYour average of 5 is " + str(round(ao5, 2)) + " seconds.")
  
  elif question == str(3):
    for i in range(0, 12):
      try:
        time_input = float(input("\nPlease input a time in seconds, seperating each one with ENTER key "))
        time_list.append(time_input) # adds the inputted value to the time list 
      except ValueError:
        print("\nInvalid input! ") 
        repeat()
    sum_of_times = sum([float(x) for x in time_list]) 
    maxnum = 0
    minnum = 0
    minnum = find_min_num(time_list)
    maxnum = find_max_num(time_list)
    three_solves = float(sum_of_times) - float(minnum) - float(maxnum) 
    ao12 = three_solves/10
    print("\nYour average of 12 is " + str(round(ao12, 2)) + " seconds.")
  elif question == str(4):
    print("\nThank you for using this program! If you have any issues be sure to put them in the project's GitHub program. ")
    raise SystemExit
  else:
    print("\nInvalid input! ")
    main()
    
  

main()
  
