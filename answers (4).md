# CMPS 6610 Problem Set 05
## Answers


**Name:**__________Yan Zhu_______________





- **1b.**

Shortest_shortest_path function, a modified version of Dijkstra’s algorithm, efficiently finds the shortest paths in a weighted graph while minimizing the number of edges when multiple paths have the same weight. For its work, the algorithm takes O((V + E) \log V), where V is the number of nodes and E is the number of edges. This is because each node and edge is processed with priority queue operations, each taking O(\log V) time.

For span, or the longest sequence of dependent operations, the algorithm has a complexity of O(V \log V). This is due to the sequential nature of priority queue operations, where each path must be individually extracted, updated, and reinserted based on minimum path weight and edge count. Thus, the algorithm is efficient for large graphs, balancing both work and span to ensure optimal path calculations with minimal edges when weights are equal.

- **3a.**
In a d-ary heap, each node has up to d children instead of the two children seen in a binary heap. This structure affects the heap’s depth: as we add levels, each level can accommodate more nodes due to the increased branching factor. Specifically, the number of elements increases by a factor of d with each level added, which allows us to reach a given number of nodes in fewer levels compared to a binary heap.

The maximum depth of a d-ary heap with n elements, then, is approximately log_d n. This depth is calculated based on how many times we can divide n by d before reaching the top level with just one root node. A larger d value results in a shallower heap, which can improve the efficiency of some operations but may also increase the cost of others, like percolating elements during insertion or deletion.

- **3b.**
In a d-ary heap, the delete-min and insert operations have different work due to the heap’s structure. For delete-min, the root element is removed, and the rightmost leaf is moved to the root position. To restore the heap property, we swap the new root downward, comparing it with each of its d children at each level. Since the heap has a depth of O(log_d n) and each level requires d comparisons, the work for delete-min is O(d*log_d(n)), or equivalently O((d/logd)*logn).

For insert, a new element is added at the rightmost leaf and swaps upward to restore the heap order. This operation only involves comparing the new element with its parent at each level, requiring O(log_d(n)) work, or O(logn/logd). So, delete-min is more costly than insert as d increases.

- **3c.**
delete-min：In the previous question, we obtained the work complexity for a single delete-min operation. For the total work of all delete-min operations in the entire algorithm, we multiply the single operation complexity O(d*log_d｜V|) by the number of times it is performed, which is |V|. This gives us a total complexity of:
O(|V|*d*log_d|V|)

insert：
This operation updates the distance to each neighbor, occurring |E| times. Each decrease-key operation in a d-ary heap is O(log_d |V|), leading to a total work of O(|E|
*log_d|V|).

The overall work bound when using a d-ary heap：
O(|V|*d*log_d|V|)+O(|E|*log_d|V|).

- **3d.**
To achieve an overall complexity of O(|E|), we need to ensure that the total work from both delete-min and decrease-key operations sums up to O(|E|). Given that |E| = |V|^（1+epsilon）, we can approximate O(|E|) \approx O(|V|).
Looking at the delete-min complexity from the previous answer, O(|V|*d*log_d |V|), we only need to show that d*log_d |V| tends towards a constant. Using the properties of logarithms:
d*log_d|V| = d*(log|V|/logd)

we choose d = |V|^epsilon, which gives:
log_d|V| = log |V|/log|V|^epsilon = log |V|/epsilon*log|V| = 1/epsilon
Thus, O(|V|*1/epsilon}) = O(|V|) = O(|E|).

Applying the same approach to the decrease-key operation, we get O(|E|*1/epsilon) = O(|E|).
Therefore, the total work calculation is:

O(|E|) + O(|E|) = O(|E|)

This reasoning confirms that our approach achieves an overall complexity of O(|E|).

- **4a.**

In this three-vertex graph, we use dynamic programming to compute all-pairs shortest paths, denoted as \text{APSP}(i, j, k), where i and j are the start and end vertices, and k represents the highest allowed intermediate vertex.

Initialization: Construct the distance matrix W with direct edge weights given, using \infty for non-existent edges. The initial matrix W is:

W =
（0 -2 2 
infinity 0 1
infinity infinity 0)


Recursive Calculation: Increment k from -1 to 2, updating \text{APSP}(i, j, k) at each step. For each pair (i, j), check if including the new intermediate vertex reduces the path length

The final result:
(0 -2 -1
infinity 0 1
infinity infinity 0)
|   | 0   | 1   | 2   |
|---|-----|-----|-----|
| 0 | 0   | -2  | -1  |
| 1 | ∞   | 0   | 1   |
| 2 | ∞   | ∞   | 0   |


This matrix shows the shortest path lengths between all vertex pairs.

- **4b.**
Yes, there’s a clear relationship between APSP(i, j, 1) and APSP(i, j, 2). In dynamic programming terms, APSP(i, j, 2) represents the shortest path from vertex i to vertex j while allowing vertices 0, 1, and 2 as intermediates. To compute APSP(i, j, 2), we can rely on previously calculated values, specifically APSP(i, j, 1) and APSP(i, 2, 1) + APSP(2, j, 1), which considers paths passing through vertex 2 as an intermediate point.

The formula is:

APSP(i, j, 2) = min(APSP(i, j, 1), APSP(i, 2, 1) + APSP(2, j, 1))


This way, APSP(i, j, 2) is calculated by either taking the shortest path from i to j that avoids vertex 2 or using the path through vertex 2 if it results in a shorter distance. This recursive structure lets us build optimal paths step-by-step, leveraging prior results without recomputing paths from scratch.

- **4c.**
If we already know all shortest paths APSP(i, j, k-1) that use vertices up to k-1, then finding APSP(i, j, k) involves two possibilities:
	1.	The shortest path from i to j doesn’t go through vertex k, so the cost is simply APSP(i, j, k-1).
	2.	Alternatively, the shortest path does go through k, in which case it’s the sum of two shorter paths: one from i to k and one from k to j, both using vertices up to k-
So, the formula becomes:
APSP(i, j, k) = min(APSP(i, j, k-1), APSP(i, k, k-1) + APSP(k, j, k-1))

This means each shortest path can be built from smaller paths, making it an optimal substructure problem where we solve by combining solutions to subproblems, just like in dynamic programming.
- **4d.**
1.In solving the APSP problem with top-down memoization, each subproblem APSP(i, j, k) represents the shortest path from vertex i to j, where only vertices 0 through k are allowed as intermediates. For a graph with n vertices, there are |V| * |V| combinations of starting and ending vertices (i, j). Additionally, each pair has n possible values of k, where k can range from 0 up to n-1. As a result, we get a total of O(|V|^3) unique subproblems that need to be computed.
  
2.With top-down memoization, each subproblem APSP(i, j, k) is computed only once and then stored. Since there are O(|V|^3) unique subproblems, and each subproblem requires a constant amount of work O(1), the total work for the algorithm is O(|V|^3). This is efficient compared to a naive approach, as memoization allows us to avoid redundant calculations, ultimately reducing the overall complexity to O(|V|^3).

- **4e.**
1.Running Dijkstra n times: For each vertex as the source, Dijkstra’s algorithm has a complexity of O(|E| log |V|), where |E| is the number of edges and |V| is the number of vertices. Therefore, running it n times gives a total complexity of O(n * |E| log |V|).
2.Dynamic Programming approach: The DP algorithm computes all possible subproblems once and has a total complexity of O(|V|^3).

In dense graphs (where |E| \approx |V|^2), the DP approach is more efficient since it avoids the extra \log |V| factor, making it faster than Dijkstra’s O(|V|^3log |V|). However, in sparse graphs (where |E| = |V|), running Dijkstra n times is more efficient, with a complexity of O(|V|^2log |V|), which is better than O(|V|^3).


- **5a.**
The MST seeks a tree that connects all nodes with the smallest possible sum of edge weights, while the MMET looks for a tree that minimizes the maximum edge weight in the tree.

A solution to the MST is not guaranteed to be a solution to the MMET because the MST prioritizes minimizing the total edge weight, without regard to the largest individual edge weight. While in some cases, the MST and MMET might be the same if minimizing the total weight also results in the smallest maximum edge weight, this isn’t always the case. There may be situations where the MST includes a higher maximum edge weight than necessary to achieve the minimum sum, meaning it’s not the optimal solution for the MMET.

- **5b.**

we can find the next best spanning tree with the following approach:

1.Compute the MST: First, find the MST of the graph using a standard algorithm, recording its total weight and edges.
2.Generate alternative MSTs: For each edge e in the original MST, temporarily remove e from the graph. Then, find the minimum spanning tree of the modified graph, which will force the tree to include a different edge to replace e.
3.rack weights: Calculate the total weight of each of these modified trees. Each tree created by removing an edge from the MST will yield a weight slightly higher than the original MST, as it introduces a new edge.
4.Choose the minimum alternative: Among all alternative MSTs created by this process, the one with the smallest weight is the second-best MST.

- **5c.**
The work of my algrothiom involves a few steps. First, we compute the MST, which takes O(|E| log |V|) using Kruskal’s. Then, for each edge in the MST (about |V| - 1 edges), we temporarily remove it and compute an alternative MST. Each alternative MST computation costs O(|E|log |V|), resulting in a total complexity of O(|V| *|E|log |V|). This ensures we find the next lowest weight tree effectively, but it can be intensive for large or dense graphs.
The work of this algorithm is O(|V| *|E|log |V|),
