for c in range(7):
  print("outer loop | c = " + str(c))
  for f in range(7):
    print("inner loop | f = " + str(f))
    if (c%2) == 0 and (f%2) == 0:
      print("Even")