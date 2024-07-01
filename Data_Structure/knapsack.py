# def knapsack_greedy(values, weights, capacity, n):
#   """
#   Solves the knapsack problem using a greedy approach based on value-to-weight ratio.

#   Args:
#       values: List of item values.
#       weights: List of item weights.
#       capacity: Maximum knapsack capacity.
#       n: Number of items.

#   Returns:
#       The total value of the selected items and the list of selected items.
#   """
#   # Calculate value-to-weight ratios
#   ratios = [value / weight for value, weight in zip(values, weights)]

#   # Sort items (values, weights, and ratios) by ratio in descending order
#   sorted_items = sorted(zip(values, weights, ratios), key=lambda x: x[2], reverse=True)

#   selected_values = []
#   selected_weights = []
#   total_value = 0
#   remaining_capacity = capacity

#   # Fill the knapsack greedily
#   for value, weight, _ in sorted_items:
#     if weight <= remaining_capacity:
#       selected_values.append(value)
#       selected_weights.append(weight)
#       total_value += value
#       remaining_capacity -= weight
#     else:
#       break  # No more items can fit

#   return total_value, selected_values, selected_weights

# # Example usage (same as before)
# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50

# total_value, selected_values, selected_weights = knapsack_greedy(values, weights, capacity, len(values))

w=[4,5,6,3,2,5,4,6,6]
p=[20,10,6,9,18,12,16,30,15]
x=[]
max_profit=30
profit=0
for i in range(len(w)):
    x.append(p[i]/w[i])
while max_profit>0:
    max_value=max(x)
    max_profit-=w[x.index(max_value)]
    profit+=p[x.index(max_value)]
    x[x.index(max_value)]=0
print("item: ",x )
print("profit: ",profit)

#Using recursion
def calc_max(p,w,c,n):
   if n==0 or c==0:
      return 0
   if(w[n-1]>c):
      return calc_max(p,w,c,n-1)
   else:
      return max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
   
w=[1,2,3]
p=[20,10,5]
c=5
n=len(p)
print(calc_max(p,w,c,n))