tree = {
  'A' : ['B', 'C'],
  'B' : ['A', 'D', 'E'],
  'C' : ['A', 'F'],
  'D' : ['B', 'G'],
  'E' : ['B', 'F'],
  'F' : ['E'],
  'G' : ['D']
}
explored = []
queue = []

def bfs(explored, tree, node):
  explored.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for child in tree[s]:
      if child not in explored:
        explored.append(child)
        queue.append(child)

bfs(explored, tree, 'A')