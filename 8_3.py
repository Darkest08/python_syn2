boat_capacity = int(input())
n_fishermen = int(input())
fishermen = list()

n_boats = 0
prev_sum = 0

for i in range(n_fishermen):
    fishermen.append(int(input()))

fishermen.sort(reverse=True)

for i in range(n_fishermen):
    if fishermen[i] != -1:
        min_diff = boat_capacity
        j_diff = i
        prev_sum = 0
        for j in range(i+1, n_fishermen):
            if fishermen[j] != -1:
                sum = fishermen[i] + fishermen[j] 
                if sum <= boat_capacity and sum > prev_sum:
                    prev_sum = sum
                    j_diff = j
        fishermen[i] = -1
        fishermen[j_diff] = -1
        n_boats+=1
print(n_boats)
