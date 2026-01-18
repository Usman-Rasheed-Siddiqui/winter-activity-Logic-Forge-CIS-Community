
def broadcast_network():
    """
    Simulate a social network broadcast system with users, follows, and messages.

    - B u m: user u broadcasts message m
    - S u v: user u starts following user v
    - U u v: user u stops following user v
    - F u: fetch last 10 messages visible to user u
    """
    
    N, Q, K = map(int, input().split())

    # Unique message ID for each broadcast
    message_id = 1
    #  Dictionary mapping user_id -> set of users they follow
    follows = {user_id: set() for user_id in range(1, N + 1)}
    messages = []   # List of all messages as tuples: (msg_id, sender, message_content, critical_flag)
    # Dictionary mapping user_id -> list of their own recent messages (max K)
    user_messages = {user_id:[] for user_id in range(1, N + 1)}

    # Process each query
    for _ in range(Q):
        order = input().split()
        
        if "B" in order:
            # Broadcast a message
            u, m = int(order[1]), int(order[2])
            critical = m % 3 == 0
            message = (message_id, u, m, critical)
            messages.append(message)
            user_messages[u].append(message)
            message_id += 1
            # Keep only last K messages for this user
            if len(user_messages[u]) > K:
                user_messages[u].pop(0)

        elif "S" in order:
            # Start following someone
            u, v = int(order[1]), int(order[2])
            follows[u].add(v)

        elif "U" in order:
            # Stop following someone
            u, v = int(order[1]), int(order[2])
            if v in follows[u]: 
                follows[u].remove(v)

        elif "F" in order:
            # Fetch feed for user u
            u = int(order[1])
            feeds = []
            # Go through all messages in reverse (latest first)
            for message in reversed(messages):
                msg_id, sender, m, critical = message
                if message in user_messages[sender]:
                    if sender == u or sender in follows[u]: # Include message if it's from self or someone user u follows
                        feeds.append(message)
                # Limit feed to last 10 messages
                if len(feeds) == 10:
                    break
            
            if not feeds:
                print("EMPTY")

            else:
                msg_ids = [str(msg[0]) for msg in feeds]
                print(" ".join(msg_ids))

broadcast_network()

