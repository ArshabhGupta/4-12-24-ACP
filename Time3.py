def test(n):
  iteration = 0
  for i in range(0, n):
    for j in range(0, n):
      print("*", end = " ")
      iteration += 1
    print(" ")
  print("\nWhen 'n' is:", n , "Iteration =" , iteration)
while True:
    a = int(input("Enter a number: "))
    test(a)

    print("With every 'n' the taken = n^2")
    print("(n^2)")
    print("Do you want to try again? (Y/N): ")
    a = input()
    if a == 'Y':
       print("Restarting Program...")
       continue
    else:
       print("Program Terminated!")
       break