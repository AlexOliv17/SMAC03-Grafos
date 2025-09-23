def BFS(listaAdj, vi):
    queue = []
    seq = []
    ids = []

    for i in range(len(listaAdj)):
        ids.append(i)
    
    queue.append(vi)
    ids.pop(vi)
    while len(queue) > 0:
        if len(queue) > 1:
            seq.append(queue[0])
            queue.pop(0)
        for valor in listaAdj[queue[0]]:
            if valor not in queue and valor in ids:
                queue.append(valor)
                ids.remove(valor)

        if len(queue) == 1 and queue[0] not in ids:
            seq.append(queue[0])
            queue.pop(0)
        

        if len(queue) == 0 and len(ids) == 1:
            seq.append(ids[0])
        elif len(queue) == 0 and len(ids) > 1:
            queue.append(ids[0])
    print(seq)


BFS({0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}, 0)