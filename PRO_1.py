def calculate(num1,num2):
  print("welcome to calculator ")
  print()
  try:
    while True:
      what = input("do you want to continue ? >>>").lower()
      if what != "yes":
          break

      num1 = float(input("enter your first number >>> "))
      print(25*"=")
      operator = input("enter your operator >>> ")
      print(25*"=")
      num2 = float(input("enter your second number >>> "))
      print(25*"=")

      match operator :
          case "+":
            print(num1 + num2)

          case "-":
            print(num1 - num2)

          case "*":
            print(num1 * num2)

          case "/":
            if num1 == 0 and num2 == 0 :
                print("mathe Error")

            else:
              print(num1 / num2)

          case "//":
            print(num1 // num2)

          case "^":
            print(num1 ** num2)

          case "%":
            print(num1 % num2)

          case _ :
            print("no is not valiade !")
  except:
    print("Math Error")





def days():
  while True:
      whe = input("do you want to continue ? >>>").lower
      if whe != "yes":
        break
      day = input("enter your day >>> ")
      match day :
        case "mon":
          print("monday")
        case "tue":
          print("tuesday")
        case "wed":
          print("wednsday")
        case "the":
          print("thersday")
        case "fri":
          print("friday")
        case "sat":
          print("saturday")
        case "sun":
          print("sunday")
        case _:
          print("enter the element")

def celsius_to_fahrenheit():
  while True:
    jefi = input("do you want to continue ? >>>").lower()
    if jefi != "yes":
        break
    kiwi = float(input("enter your celesieus >>> "))
    print(32 + 1.8 * kiwi,"F°")

# 2k or 2k +1 

def number():
  try:
    while True:
      xcv = input("do you want to continue ? >>>").lower()
      if xcv != "yes":
        break
      numb = float(input("enter your number Here >>> "))
      if numb % 2 == 0:
        print("2K")
      else:
        print("2K + 1 ")

  except ValueError:
    print("Math Error!")


print("\033[34m""Mini Assisstance pro ""\033[0m")

print("1.CALCULATOR\n2.DAYS\n3.C° to F\n4.2k or 2k +1\n5.Close")
print(20*"=")
print()
Mini_Assisstance_PRO = int(input("chose number 1 to 5 >>> "))
match Mini_Assisstance_PRO:
  case 1:
    calculate(0,0)
  case 2:
    days()
  case 3:
    celsius_to_fahrenheit()
  case 4 :
    number()
  case 5 :
    print("good bye")




