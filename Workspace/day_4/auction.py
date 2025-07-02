
print("Welcome to the secret auction program.")
first_bidder=input("What is your name? ")
first_bid=int(input("What is your bid? $"))
bids={
    first_bidder:first_bid
}
more_bidder=input("Are there any other bidders? type 'yes' or 'no'").lower()

if more_bidder=="yes":
    auction_on=True
else:
    auction_on=False
while(auction_on):
    print("\n"*100)
    new_bidder=input("What is your name? ")
    new_bid=int(input("What is your bid? $"))
    bids[new_bidder]=new_bid
    more_bidder=input("Are there any other bidders? type 'yes' or 'no'").lower()
    if more_bidder=="no":
        auction_on=False

highest_bid