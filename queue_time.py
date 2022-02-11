def queue_time(customers, n):
    queues = [0] * n
    for i in customers:
        queues[0] += i
        queues.sort()
        print(queues)
    return max(queues)


print(queue_time([2,3,4,5,10], 2))