from replit import clear
import art

print(art.logo)
game_end=False
store_dict={}
while not game_end:
    print("Welcome to the Secret Auction Program")
    name=input("What's your name ? :\n")
    bid=int(input("What's your bid ($) ? :\n"))
    store_dict[name]=bid
    game_progress=input("Are there any other bidders ? Type 'yes' or 'no'.\n").lower()
    if(game_progress=="no"):
        game_end=True
    clear()
max_bid=0
for name in store_dict:
    if(store_dict[name]>max_bid):
        max_bid=store_dict[name]
        highest_payee=name
print(f"The winner is {highest_payee} with a bid of ${max_bid}")
print("Thank you!")
    
