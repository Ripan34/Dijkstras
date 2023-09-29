import heapq
import matplotlib.pyplot as plt
import networkx as nx

start_vert = 0
end_vert = 0
total_vert = 0
graphHolder = {}
edges = []

with open("input.txt", "r") as inputFile:
    total_vert = int(inputFile.readline().rstrip())
    start_vert = int(inputFile.readline().rstrip())
    end_vert = int(inputFile.readline().rstrip())

    for line in inputFile:
        edge = line.rstrip().split(' ')
        source = int(edge[0])
        target = int(edge[1])
        edges.append((source, target))
        weight = float(edge[2])
        if source not in graphHolder:
            graphHolder[source] = {}
        if target not in graphHolder:
            graphHolder[target] = {}
        graphHolder[source][target] = weight
x = []
y = []
G = nx.Graph()

with open("coords.txt", "r") as cordFile:
    for line in cordFile:
        ln = line.rstrip().split(' ')
        x.append(float(ln[0]))
        y.append(float(ln[1]))

table = {node: (float("inf"), 0) for node in graphHolder}
shortestPath = []
weights = []
table[start_vert] = (0, 0.0)
minHeap = [(0, start_vert, 0.0)]
heapq.heapify(minHeap)

ind = 0
while minHeap:
    currWeight, currVert, prevVert = heapq.heappop(minHeap)
    # if not G.has_node(currVert):
    #     G.add_node(currVert)
    #point1 = [x[currVert-1], y[currVert-1]]
    neighborList = sorted(graphHolder[currVert].items())
    for neighbor in dict(neighborList):
        updatedWeight = currWeight + graphHolder[currVert][neighbor]
        if updatedWeight < table[neighbor][0]:
            table[neighbor] = (updatedWeight, currVert)
            heapq.heappush(minHeap, (updatedWeight, neighbor, currVert))
            # if not G.has_edge(currVert, neighbor):
            #     G.add_edge(currVert, neighbor)
            # nx.draw(G, pos, with_labels=True, node_color='skyblue', font_weight='bold')
            # plt.savefig(f'pics/pic{ind}')
            # if ind != 97:
            #     plt.clf()
            # ind += 1
    #     point2 = [x[neighbor-1], y[neighbor-1]]
    # x_values = [point1[0], point2[0]]
    # y_values = [point1[1], point2[1]]
    #plt.plot(x_values, y_values, 'bo', linestyle="-", color='black')

shortestPath.append(end_vert)
weights.append(table[end_vert][0])
#nx.draw(G, with_labels=True, node_color='skyblue')
while end_vert != start_vert:
    shortestPath.insert(0, table[end_vert][1])
    weights.insert(0, table[end_vert][0])
    end_vert = table[end_vert][1]

weights.insert(0, 0)
weights = [round(x, 4) for x in weights]
points = []
for ele in shortestPath:
    points.append([x[ele-1], y[ele-1]])

# for i in range(len(points)-1):
#     point1 = points[i]
#     point2 = points[i+1]
#     x_values = [point1[0], point2[0]]
#     y_values = [point1[1], point2[1]]
#     plt.plot(x_values, y_values, 'bo', linestyle="-", color='red')
#     plt.savefig(f'pics/pic{ind}')
#     ind += 1
# plt.show()

outputShortest = [str(x) for x in shortestPath]
outputWeights = [str(x) for x in weights]
outputFile = open('output.txt', 'w')
outputFile.write(' '.join(outputShortest))
outputFile.write('\n')
outputFile.write(' '.join(outputWeights))
outputFile.close()