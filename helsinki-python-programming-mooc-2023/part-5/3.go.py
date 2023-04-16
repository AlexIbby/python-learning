# Write your solution here

def who_won(game_board:list):

    player_one_count = 0
    player_two_count = 0

    for item in game_board:
        one_count = item.count(1)
        two_count = item.count(2)

        player_one_count += one_count
        player_two_count += two_count

    if player_one_count > player_two_count:
        return 1
    elif player_two_count > player_one_count:
        return 2
    else:
        return 0

    