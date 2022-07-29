
def unboundedKnapsack(W, index, val, wt):
	if index==0:
    return (W//wt[0])*val[0]
	
	notTake=0+unboundedKnapsack(W,index-1,val,wt)
	take=-100000
	if wt[index]<=W:
		take=val[index]+unboundedKnapsack(W-wt[index],index,val,wt)
	return max(take,notTake)


W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)

print(unboundedKnapsack(W, n-1, val, wt))
