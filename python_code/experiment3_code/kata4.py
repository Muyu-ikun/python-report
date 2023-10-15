def recoverSecret(triplets):
    # 构建字母之间的关系图
    graph = {}
    for triplet in triplets:
        for letter in triplet:
            if letter not in graph:
                graph[letter] = set()
    
    for triplet in triplets:
        graph[triplet[0]].add(triplet[1])
        graph[triplet[1]].add(triplet[2])
    
    # 使用拓扑排序找出字母的正确顺序
    visited = set()
    result = []
    
    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                visit(neighbor)
            result.insert(0, node)
    
    for letter in graph:
        visit(letter)
    
    return ''.join(result)