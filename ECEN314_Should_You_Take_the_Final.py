while (True):
  print("ECEN314 Should You Take the Final, a Jack Begeman Script\n\n\n")


  print("Enter in all homeworks that have been graded.\n")
  homeworkholder = []
  homeworkholder.append(int(input("Homework1 (out of 100): ")))
  homeworkholder.append(int(input("Homework2 - Part1 (out of 40): ")) / 40 * 100)
  homeworkholder.append(int(input("Homework2 - Part2 (out of 60): ")) / 60 * 100)
  homeworkholder.append(int(input("Homework3 (out of 50): ")) / 50 * 100)
  homeworkholder.append(int(input("Homework4 (out of 40): ")) / 40 * 100)
  homeworkholder.append(int(input("Homework5 (out of 40): ")) / 40 * 100)
  homeworkholder.append(int(input("Homework6 (out of 50): ")) / 50 * 100)
  homeworkholder.append(int(input("Homework7 (out of 50): ")) / 50 * 100)
  homeworkholder.append(int(input("Homework8 (out of 100): ")) / 100 * 100)
  homeworkholder.append(int(input("Homework9 (out of 50): ")) / 50 * 100)

  print("\n\nEnter in all 3 midterm grades.\n")
  examholder = []
  for i in range(3):
       examholder.append(int(input("Exam {} (out of 100): ".format(i + 1))))

  print(
      "\n\nAssuming your average on homeworks stays the same if you inputted less than all homeworks..."
  )

  examavg = sum(examholder) / 3
  homeworkavg = sum(homeworkholder) / 10
  Grade = (examavg * .75) + (homeworkavg * .25)
  print("Current Exam Avg: {:.2f}%".format(examavg))
  print("Current Homework Avg: {:.2f}%".format(homeworkavg))
  print("Current Grade: {:.2f}%\n".format(Grade))

  examholder.remove(min(examholder))

  while (True):
    if (Grade >= 89):
      print(
          "You have an A! Don't take the final, unless you want to take a victory lap."
      )
      break
    print("To get an A, you need a {:.2f}% on the final".format(89 / 0.25 -
                                                                examholder[0] -
                                                                examholder[1] -
                                                                homeworkavg))
    if (Grade >= 79):
      print(
          "You have secured a B, if you are good with a B and don't want to go for the A, don't take the final. But you probably should take the final."
      )
      break
    print("To get a B, you need a {:.2f}% on the final".format(77 / 0.25 -
                                                               examholder[0] -
                                                               examholder[1] -
                                                               homeworkavg))
    if (Grade >= 65):
      print(
          "You are guaranteed to pass the class with a C, but you should probably take the final to try and get something higher."
      )
      break
    print("To pass the class, you need a {:.2f}% on the final".format(
        65 / 0.25 - examholder[0] - examholder[1] - homeworkavg))
    if (Grade < 65):

      print("You should have q dropped")
      skull = '''
      ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠴⠶⠶⠶⠶⠶⠶⠶⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⢀⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀
      ⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⡄⠀⠀⠀
      ⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀
      ⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀
      ⣿⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⢹⡄
      ⡏⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇
      ⣿⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⢸⡇
      ⢹⡆⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⣾⠀
      ⠈⢷⡀⢸⡇⠀⢀⣠⣤⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⢀⣠⣶⣶⣶⣶⣤⣄⠀⠀⣿⠀⣼⠃⠀
      ⠀⠈⢷⣼⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⡾⠃⠀⠀
      ⠀⠀⠈⣿⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⡇⠀⠀⠀
      ⠀⠀⠀⣿⠀⠀⠘⢿⣿⣿⣿⣿⡿⠃⠀⢠⠀⣄⠀⠀⠙⢿⣿⣿⣿⡿⠏⠀⠀⢘⡇⠀⠀⠀
      ⠀⠀⠀⢻⡄⠀⠀⠀⠈⠉⠉⠀⠀⠀⣴⣿⠀⣿⣷⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢸⡇⠀⠀⠀
      ⠀⠀⠀⠈⠻⣄⡀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠘⣟⠳⣦⡀⠀⠀⠀⠸⣿⡿⠀⢻⣿⡟⠀⠀⠀⠀⣤⡾⢻⡏⠁⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⢻⡄⢻⠻⣆⠀⠀⠀⠈⠀⠀⠀⠈⠀⠀⠀⢀⡾⢻⠁⢸⠁⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⢸⡇⠀⡆⢹⠒⡦⢤⠤⡤⢤⢤⡤⣤⠤⡔⡿⢁⡇⠀⡿⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠘⡇⠀⢣⢸⠦⣧⣼⣀⡇⢸⢀⣇⣸⣠⡷⢇⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠺⣄⣇⢸⠉⡏⢹⠉⡏⢹⢀⣧⠾⠋⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠈⠉⠙⠓⠚⠚⠋⠉⠁⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠶⠦⣤⣤⣤⡤⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      '''
      print(skull)
      break
  if("n" == input("Would you like to go again? (y/n):")):
      break