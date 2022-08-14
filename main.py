while True:

  inp = input("please enter a number")
  if inp.isdigit():
        inp=int(inp)
        if inp % 2 != 0:
          print(inp,"is and odd number")
        else:
           print("even number")
  else:
        print("error")