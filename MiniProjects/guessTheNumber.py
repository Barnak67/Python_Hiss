import random

def scoreGen(rno, multiplier, chances):
       score = 100
       attempt = 1
       while attempt <= chances:
      
              userCh = input("Enter a number you want to guess!, to quit Enter 'Q': ")
              if userCh == "Q" or userCh == "q":
                  print("Thanks for playing, Visit again!")
                  return
              userCh = int(userCh)
      
              if (userCh == rno) :
                  print("-" * 30)
                  print(f"Congrats! you guess the right number! in {attempt} attempts")
                  print(f"Your score is {score * multiplier}")
                  return
      
              elif (userCh > rno) :
                          print("Wrong Choice! Think of a lower number")
                          print(f"Your Attempt: {attempt}")
                          attempt += 1
                          score -= 1
      
              elif (userCh < rno) :
                          print("Wrong Choice! Think of a higher number")
                          print(f"Your Attempt: {attempt}")
                          attempt += 1
                          score -= 1 


print("======GUESS THE NUMBER======")
print("Welcome to guess the number game...\n" \
"Every time you miss-guess one point will be deducted\n" \
"In order to win you have to guess a number between 1-100")

target = random.randint(1, 100)

print("Choose your difficulty:")
print("1: Easy -> Unlimited Chances")
print("2: Medium -> 10 Chances, 2x Points")
print("3: Hard -> 3 Chances, 5x Points")
print("4: QUIT")

ch  = int(input("Enter your Choice: "))

while True:
    match ch:
        case 1:
            print("------Welcome to the Easy Mode------")
            scoreGen(target, 1, 100000)
            break
        case 2: 
            print("------Welcome to the Medium Mode------")
            scoreGen(target, 2, 10)
            break
        case 3:
            print("------Welcome to the Hard Mode------")
            scoreGen(target, 5, 3)
            break
        case 4:
            print("Thanks for visiting!")
            break
        case _:
             print ("Wrong Choice")
             break