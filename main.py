print("Exam Grade Generator")
print("---------------")

print()

examClass = input("Name of exam: ")

print()

maxScore = float(input("Maximum possible score: "))

print()

scoreMarked = float(input("Your score: "))

print()

yourScore = round(scoreMarked / maxScore * 100 , 2)

print()

if yourScore >= 90 and yourScore <= 100:
  print(f"Your score is {yourScore}. You scored a A+")
elif yourScore >= 80 and yourScore <= 89:
  print(f"Your score is {yourScore}. You scored a A")
elif yourScore >= 70 and yourScore <= 79:
  print(f"Your score is {yourScore}. You scored a B")
elif yourScore >= 60 and yourScore <= 69:
  print(f"Your score is {yourScore}. You scored a C")
elif yourScore >= 50 and yourScore <= 59:
  print(f"Your score is {yourScore}. You scored a D")
elif yourScore <= 49:
  print(f"Your score is {yourScore}. You scored a U")
else:
  print("Error, please enter correct infomation.")
