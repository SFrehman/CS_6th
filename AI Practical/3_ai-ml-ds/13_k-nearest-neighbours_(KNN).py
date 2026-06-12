import math
import matplotlib.pyplot as plt

# Function to calculate Euclidean distance
def euclidean_dist(x,y):
    sum=0                                    
    for i in range(len(x)):                  
        sum += (x[i] - y[i])**2              
    return math.sqrt(sum)                    

# Store points belonging to two groups
points = {
    'group1': [[3,5], [4,5], [3,6], [2,6]],
    'group2': [[7,3], [5,5], [7,5], [7,6], [6,3]],
}

# Separate x and y coordinates of group1
x1,y1 = zip(*points['group1'])

# Separate x and y coordinates of group2
x2,y2 = zip(*points['group2'])

# Plot group1 points
plt.scatter(x1,y1)

# Plot group2 points
plt.scatter(x2,y2)

# Define new point to classify
new_point = [3,3]

# Plot new point
plt.scatter(3,3)

# Display graph
plt.show()

# Store distances and corresponding groups
nn_dist = []

# Loop through each group
for group in points:

    # Loop through each point in current group
    for point in points[group]:

        # Calculate distance between point and new point
        dist = euclidean_dist(point, new_point)

        # Store distance and group name
        nn_dist.append([dist, group])

# Display distances sorted from nearest to farthest
print(sorted(nn_dist))