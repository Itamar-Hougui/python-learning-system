import os

print("Welcome to the secret auction program.")
first_bidder=input("What is your name? ")
first_bid=int(input("What is your bid? $"))
bids={
    first_bidder:first_bid
}
more_bidder=input("Are there any other bidders? type 'yes' or 'no'").lower()
highest_bid=bids[first_bidder]
highest_bider=first_bidder
if more_bidder=="yes":
    auction_on=True
else:
    auction_on=False
while(auction_on):
    os.system('clear')
    new_bidder=input("What is your name? ")
    new_bid=int(input("What is your bid? $"))
    bids[new_bidder]=new_bid
    more_bidder=input("Are there any other bidders? type 'yes' or 'no'").lower()
    if more_bidder=="no":
        auction_on=False

for name in bids:
    if (bids[name]>highest_bid):
        highest_bid=bids[name]
        highest_bider=name
print(f"The highest bidder is {highest_bider}\nWho bids ${highest_bid}")