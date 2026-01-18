
def broadcast_network():
    
    N, Q, K = map(int, input().split())

    message_id = 1
    follows = {user_id: set() for user_id in range(1, N + 1)}
    messages = []
    user_messages = {user_id:[] for user_id in range(1, N + 1)}

    
    for _ in range(Q):
        order = input().split()
        
        if "B" in order:
            u, m = int(order[1]), int(order[2])
            critical = m % 3 == 0
            message = (message_id, u, m, critical)
            messages.append(message)
            user_messages[u].append(message)
            message_id += 1

            if len(user_messages[u]) > K:
                user_messages[u].pop(0)

        elif "S" in order:
            u, v = int(order[1]), int(order[2])
            follows[u].add(v)

        elif "U" in order:
            u, v = int(order[1]), int(order[2])
            if v in follows[u]: 
                follows[u].remove(v)

        elif "F" in order:
            u = int(order[1])
            feeds = []

            for message in reversed(messages):
                msg_id, sender, m, critical = message
                if sender == u or sender in follows[u]:
                    feeds.append(message)
                
                if len(feeds) == 10:
                    break
            
            if not feeds:
                print("EMPTY")

            else:
                msg_ids = [str(msg[0]) for msg in feeds]
                print(" ".join(msg_ids))

broadcast_network()

