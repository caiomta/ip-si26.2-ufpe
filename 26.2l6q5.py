# TODO: implementar checagem de abertura clássica


def main():
    print(
        "Ho ho ho! Quem ousa desafiar o Papai Noel numa partida de xadrez de "
        "Natal?"
    )

    child_name = input()

    if child_name == "Beth Harmon":
        print("Nossa, temos um gênio aqui")
    elif child_name == "Magnus Carlsen":
        print("Essa vai ser difícil! O menino é um prodígio!")

    print("Que a partida comece! O Papai Noel joga com as peças brancas.")

    board = generate_board()
    hist = []
    play(board, hist, child_name)


def generate_board():
    column_pieces = ("t", "c", "b", "d", "r", "b", "c", "t")
    board = {}
    for j in range(8):
        board[1, j], board[6, j] = "p", "P"
        board[0, j], board[7, j] = column_pieces[j], column_pieces[j].upper()
    return board


def play(board, hist, child_name, turn=0):
    info = input()
    player, origin, dest = info.split()
    player_name = "Papai Noel" if player == "N" else child_name

    if is_wrong_player(turn, player):
        register_move(hist, player_name, origin, "FORA DA VEZ")

        print(
            f"{player_name} insistiu em jogar fora da vez! A partida foi "
            "encerrada."
        )
        return

    origin, dest = (
        tuple(int(i) for i in origin.strip("()").split(", ")),
        tuple(int(i) for i in dest.strip("()").split(", ")),
    )

    if is_move_valid(board, player, origin, dest):
        if is_king_in_dest(board, dest):
            winner = child_name if turn % 1 else "Papai Noel"
            print(f"O rei foi capturado! {child_name} venceu a partida!")
            return
        move(board, origin, dest)
    else:
        print("Jogada errada, perdeu a vez!")

    return play(board, turn + 1)


def is_wrong_player(r, player):
    return (r == 0 and player != "N") or player == "N"


def is_king_in_dest(board, dest):
    return board.get(dest, "").lower() == "r"


def move(board, origin, dest):
    board[dest] = board[origin]
    del board[origin]


def is_move_valid(board, player, origin, dest):
    if not are_all_coordinates_in_board_range(origin, dest):
        return False

    origin_p, dest_p = board.get(origin, ""), board.get(dest, "")
    if not is_piece_from_player(origin_p, player) or is_piece_from_player(
        dest_p, player
    ):
        return False

    return IS_PIECE_MOVEMENT_VALID[origin_p.lower()](board, origin, dest)


def are_all_coordinates_in_board_range(origin, dest):
    for c in origin + dest:
        if not (0 <= c < 8):
            return False
    return True


def is_piece_from_player(piece, player):
    if player == "N":
        return piece.isupper()
    return piece.islower()


def is_tower_movement_valid(board, _player, origin, dest):
    dir_i = get_direction_index_if_straight(origin, dest)
    if dir_i == -1:  # not straight
        return False
    return is_line_free(board, dir_i, origin, dest)


def is_horse_movement_valid(_board, _player, origin, dest):
    abs_v_diff = abs(origin[0] - dest[0])
    abs_h_diff = abs(origin[1] - dest[1])
    return (abs_v_diff, abs_h_diff) in ((1, 2), (2, 1))


def is_bishop_movement_valid(board, _player, origin, dest):
    if not is_movement_diagonal(origin, dest):
        return False
    return is_diagonal_free(board, origin, dest)


def is_queen_movement_valid(board, _player, origin, dest):
    if is_movement_diagonal(origin, dest):
        return is_diagonal_free(board, origin, dest)

    dir_i = get_direction_index_if_straight(origin, dest)
    if dir_i == -1:  # not straight
        return False
    return is_line_free(board, dir_i, origin, dest)


def is_king_movement_valid(_board, _player, origin, dest):
    return abs(origin[0] - dest[0]) in (0, 1) and abs(origin[1] - dest[1]) in (
        0,
        1,
    )


def is_pawn_movement_valid(board, player, origin, dest):
    v_diff = dest[0] - origin[0]

    if (
        (not (0 < abs(v_diff) < 3))  # moved too much
        or (player == "N" and v_diff > 0)
        or (v_diff < 0)  # moved backwards
    ):
        return False

    dest_p = board.get(dest)

    if is_movement_diagonal(origin, dest) and (
        abs(v_diff) != 1  # excessive diagonal movement
        or not dest_p  # non-offensive diagonal
        or is_piece_from_player(dest_p, player)  # friendly-fire diagonal
    ):
        return False

    piece_in_front = (origin[0] - v_diff / abs(v_diff), origin[1]) in board
    if dest in board or piece_in_front:  # piece at or in between destination
        return False

    return True


IS_PIECE_MOVEMENT_VALID = {
    "t": is_tower_movement_valid,
    "c": is_horse_movement_valid,
    "b": is_bishop_movement_valid,
    "d": is_queen_movement_valid,
    "r": is_king_movement_valid,
    "p": is_pawn_movement_valid,
}


def is_movement_diagonal(origin, dest):
    return abs(origin[0] - dest[0]) == abs(origin[1] - dest[1])


def is_movement_straight(origin, dest):
    return origin[0] == dest[0] or origin[1] == dest[1]


def get_direction_index_if_straight(origin, dest, default=-1):
    if not is_movement_straight(origin, dest):
        return default
    return 0 if origin[0] != dest[0] else 1


# checa se a diagonal tem alguma peça de maneira otimista
# (espera que origem-destino realmente seja uma diagonal, sem checar)
def is_diagonal_free(board, origin, dest):
    abs_diff = abs(origin[0] - dest[0])
    v_dir, h_dir = (
        1 if dest[0] > origin[0] else -1,
        1 if dest[1] > origin[1] else -1,
    )
    for step in range(1, abs_diff):
        if (origin[0] + step * v_dir, origin[1] + step * h_dir) in board:
            return False
    return True


def is_line_free(board, dir_i, origin, dest):
    iter_dir = 1 if dest[dir_i] > origin[dir_i] else -1
    abs_diff = abs(dest[dir_i] - origin[dir_i])
    for step in range(1, abs_diff):
        coord = (
            (origin[0] + step * iter_dir, origin[1])
            if dir_i == 0
            else (origin[0], origin[1] + step * iter_dir)
        )
        if coord in board:
            return False
    return True


def register_valid_move(hist, name, origin, dest):
    register_move(hist, name, origin, dest, "VÁLIDA")


def register_wrong_move(hist, name, origin, dest):
    register_move(hist, name, origin, dest, "ERRADA")


def register_wrong_turn_move(hist, name, origin, dest):
    register_move(hist, name, origin, dest, "FORA DA VEZ")


def register_move(hist, name, origin, dest, status):
    hist.append(
        {
            "name": name,
            "origin": origin,
            "dest": dest,
            "status": status,
        }
    )
