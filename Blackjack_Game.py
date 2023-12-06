import random
import art_for_blackjack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]
user_cards = []
computer_cards = []

def game_on():
  print(art_for_blackjack.logo)
  print("WELCOME TO BLACKJACK GAME!")
  def deal():
    return random.choice(cards)
  user_cards.append(deal())
  user_cards.append(deal())
  computer_cards.append(deal())
  computer_cards.append(deal())
  print(f"User cards: {user_cards}")
  print(f"Computer cards: {computer_cards}")
  def calculate_score(list_of_cards):
    if 11 in list_of_cards and 10 in list_of_cards:
      return 0
    elif 11 in list_of_cards and sum(list_of_cards) > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
    return sum(list_of_cards)
  users_score = calculate_score(user_cards)
  computers_score = calculate_score(computer_cards)
  print(f"User's score: {users_score}")
  print(f"Computer's score: {computers_score}")
  if computers_score == 0:
    print("Computer has a blackjack, you lost.")
  elif users_score == 0:
    print("You have a blackjack, you WIN!")
  else:
    while (users_score<21 and computers_score<21):
      if users_score == 0 or computers_score == 0:
        print(f"User cards: {user_cards}, Computer's cards: {computer_cards}")
        print(f"User's score: {users_score},Computer's score: {computers_score}")
        break
      another_draw = input("Would you like to get another card? Type y or n:\n").lower()
      if another_draw == "y":
        user_cards.append(deal())
        users_score=calculate_score(user_cards)
    
      if another_draw == "n":
        while computers_score < 17:
          computer_cards.append(deal())
          computers_score = calculate_score(computer_cards)
          #print(computers_score)
        if computers_score>=17:
          print(f"User cards: {user_cards}, Computer's cards: {computer_cards}")
          print(f"User's score: {users_score},Computer's score: {computers_score}")
          break
      
      print(f"User cards: {user_cards}, Computer's cards: {computer_cards}")
      print(f"User's score: {users_score}, Computer's score: {computers_score}")
    def compare(computers_score, users_score):
      if computers_score == 0:
        print("Computer has a blackjack, you lost.")
      elif users_score == 0:
        print("You have a blackjack, you WIN!")
      elif computers_score == users_score:
        print("It's a draw!")
      elif computers_score == 0 or users_score>21:
        print("Computer wins, You lost.")
      elif users_score == 0 or computers_score>21:
        print("You win!")
      else:
        if computers_score>users_score:
          print("Computer wins, You lost")
        elif users_score>computers_score:
          print("You win!")
    compare(computers_score, users_score)
    
  print("Game ended.")
  again = input("Would you like to play again? Type y or n:\n").lower()
  if again == "y":
    computer_cards.clear()
    user_cards.clear()
    game_on()
game_on()
      
      



  