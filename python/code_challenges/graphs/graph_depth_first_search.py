Class depth_first(graph, next)

	list = []

	visited = set()

	stack = Stack()

	while stack:

		head = stack.pop()

		if stack in visited:

			continue

		yield head

		visited.add(head)

		for child in graph[head]:

			stack.append(child)
