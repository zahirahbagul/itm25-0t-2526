def relationship_status(from_member, to_member, social_graph):
    follows_from = social_graph[from_member]["following"]
    follows_to = social_graph[to_member]["following"]

    both_follow = from_member in follows_to and to_member in follows_from
    only_from = to_member in follows_from
    only_to = from_member in follows_to

    if both_follow:
        return "friends"
    elif only_to:
        return "followed by"
    elif only_from:
        return "follower"
    else:
        return "no relationship"

def tic_tac_toe(board):
    board_size = len(board)
    consecutive = 0

    for row in range(board_size):
        consecutive = 0
        for col in range(board_size - 1):
            if board[row][col] == board[row][col + 1] and board[row][col] != "":
                consecutive += 1
            else:
                break
        if consecutive == board_size - 1:
            return board[row][0]

    for col in range(board_size):
        consecutive = 0
        for row in range(board_size - 1):
            if board[row][col] == board[row + 1][col] and board[row][col] != "":
                consecutive += 1
            else:
                break
        if consecutive == board_size - 1:
            return board[0][col]

    consecutive = 0
    for index in range(board_size - 1):
        if board[index][index] == board[index + 1][index + 1] and board[index][index] != "":
            consecutive += 1
        else:
            break
    if consecutive == board_size - 1:
        return board[0][0]
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for segment in route_map:
            if segment[0] == current_stop:
                total_time += route_map[segment]["travel_time_mins"]
                current_stop = segment[1]
                break

    return total_time
