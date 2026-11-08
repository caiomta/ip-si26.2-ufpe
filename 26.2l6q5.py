PLAYER_ORDER = ("N", "C")


FAMOUS_OPENINGS = {
    (
        ((6, 4), (4, 4)),
        ((1, 2), (3, 2)),
    ): "a Defesa Siciliana",
    (
        ((6, 4), (4, 4)),
        ((1, 3), (3, 3)),
    ): "a Defesa Escandinava",
    (
        ((6, 3), (4, 3)),
        ((1, 3), (3, 3)),
        ((6, 2), (4, 2)),
    ): "o Gambito da Rainha",
}


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
    winner = play(board, hist, child_name)
    print_history(hist)

    if winner == child_name:
        print(
            f"Parabéns, {child_name}! Você venceu o Papai Noel e ganhou um "
            "presente!"
        )
    else:
        print(
            f"Ho ho ho! Você não foi uma criança boa durante o ano, "
            f"{child_name}, e por isso perdeu. Sem presente!"
        )


def generate_board():
    column_pieces = ("t", "c", "b", "d", "r", "b", "c", "t")
    board = {}
    for j in range(8):
        board[1, j], board[6, j] = "p", "P"
        board[0, j], board[7, j] = column_pieces[j], column_pieces[j].upper()
    return board


def play(board, hist, child_name, turn=0):
    move_info = input()
    player, origin, dest = extract_move_info(move_info)

    if not is_right_player(turn, player):
        register_wrong_turn_move(hist, player, child_name, origin, dest)
        print(
            f"{get_player_name(player, child_name)} insistiu em jogar fora da "
            "vez! A partida foi encerrada."
        )
        return get_opposite_player_name(player, child_name)

    if is_move_valid(board, player, origin, dest):
        register_valid_move(hist, player, child_name, origin, dest)
        check_famous_opening(hist, player, child_name)

        if check_mate(board, dest):
            player_name = get_player_name(player, child_name)
            print(f"O rei foi capturado! {player_name} venceu a partida!")
            return player_name

        move(board, origin, dest)
    else:
        register_wrong_move(hist, player, child_name, origin, dest)
        print("Jogada errada, perdeu a vez!")

    return play(board, hist, child_name, turn + 1)


def check_mate(board, dest):
    return board.get(dest, "").lower() == "r"


def extract_move_info(move_str):
    player, coords_str = move_str.split(maxsplit=1)
    origin_y, origin_x, dest_y, dest_x = [
        int(c.strip("(),")) for c in coords_str.split()
    ]
    return player, (origin_y, origin_x), (dest_y, dest_x)


def get_player_name(player, child_name):
    return "Papai Noel" if player == "N" else child_name


def get_opposite_player_name(player, child_name):
    return child_name if player == "N" else "Papai Noel"


def is_right_player(turn, player):
    return PLAYER_ORDER[turn % 2] == player


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

    return IS_PIECE_MOVEMENT_VALID[origin_p.lower()](
        board, player, origin, dest
    )


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
    positive_v_diff = v_diff > 0

    if (
        (not (0 < abs(v_diff) < 3))  # moved too much
        or (player == "N" and positive_v_diff)
        or (player == "C" and not positive_v_diff)
    ):
        return False

    if origin[1] != dest[1]:
        dest_p = board.get(dest)
        h_diff = dest[1] - origin[1]
        return (
            abs(v_diff) == 1
            and abs(h_diff) == 1
            and dest_p
            and not is_piece_from_player(dest_p, player)
        )

    if abs(v_diff) == 1:
        return dest not in board
    return not (
        dest in board
        or (origin[0] + (1 if positive_v_diff else -1), origin[1]) in board
    )


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


def register_valid_move(hist, player, child_name, origin, dest):
    register_move(hist, player, child_name, origin, dest, "VÁLIDA")


def register_wrong_move(hist, player, child_name, origin, dest):
    register_move(hist, player, child_name, origin, dest, "ERRADA")


def register_wrong_turn_move(hist, player, child_name, origin, dest):
    register_move(hist, player, child_name, origin, dest, "FORA DA VEZ")


def register_move(hist, player, child_name, origin, dest, status):
    hist.append(
        {
            "player_name": get_player_name(player, child_name),
            "origin": origin,
            "dest": dest,
            "status": status,
        }
    )


def print_history(hist):
    print("Histórico da partida:")
    for i, move in enumerate(hist):
        print(
            f"{i + 1}. {move['player_name']}: {move['origin'][0]} "
            f"{move['origin'][1]} -> {move['dest'][0]} {move['dest'][1]} "
            f"[{move['status']}]"
        )


def check_famous_opening(hist, player, child_name):
    hist_tuple = tuple(
        (i["origin"], i["dest"]) for i in hist if i["status"] == "VÁLIDA"
    )

    if len(hist_tuple) not in (2, 3):
        return

    for moves in FAMOUS_OPENINGS:
        if moves == hist_tuple:
            print(
                f"Muito bem, {get_player_name(player, child_name)} utilizou "
                f"{FAMOUS_OPENINGS[moves]}!"
            )


main()
