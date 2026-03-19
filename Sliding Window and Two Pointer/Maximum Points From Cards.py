#Maximum points must be obtained from picking cards from either direction(left or right) in an array 
#number of cards to be picked will be given and cards must be picked from any end and not from middle
print("enter number of cards")
n=int(input())
print("enter the card values")
cards = list(map(int, input().split()))
if len(cards) != n:
    print(f"Error: Expected {n} numbers, but got {len(cards)}.")
else:
    print("enter the number of cards which can be picked")
    k=int(input())
    def check(cards,k):
        lsum=0
        rsum=0
        for i in range(0,k):
            lsum=lsum+cards[i]
        rindex=n-1
        maxsum=lsum
        for i in range(k-1,-1,-1):
            lsum=lsum-cards[i]
            rsum=rsum+cards[rindex]
            rindex=rindex-1
        maxsum=max(maxsum,lsum+rsum)
        return maxsum
    print("max sum is",check(cards,k))