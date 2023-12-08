from replit import clear

from art import logo
print(logo)


game = True
data = []
players = [] 
winner = ""

while game:
  name = input("Name: ")
  bid = int(input("Bid: $"))
  
  newdata = {"name":name, "bid":bid}
  data.append(newdata)

  choice = input("Do you want to continue?(Yes/No): ").lower()

  if choice == "yes":
    clear()
  else:
    for dick in data:
      for key in dick:
        players.append(dick["bid"])
    game = False

points = max(players)

for n in data:
  if n["bid"] == points:
    winner = n["name"]
    break

print(f"The winner is {winner} who bid ${points}")
