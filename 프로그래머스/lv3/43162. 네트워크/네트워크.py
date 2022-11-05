def solution(n, computers):
    visited = []
    intranet = []
    network = []
    def connect(node):
        visited.append(node)
        intranet.append(node)
        for nextnode in range(n):
            if nextnode not in visited and computers[node][nextnode]==1:
                connect(nextnode)
        return intranet
    
    for node in range(n):
        if node not in visited:
            network.append(connect(node))
            intranet = []
    return len(network)
                
