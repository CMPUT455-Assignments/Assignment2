from board_util import GoBoardUtil
INFINITY = 999999999

def alphabeta(state, alpha, beta, tt, zobrist):
    hashCode = zobrist.hash(GoBoardUtil.get_oneD_board(state))
    result = tt.search(hashCode)

    if result is not None:
        return result

    if state.end_of_game():
        result = state.evaluate(), None
        saveResult(tt, hashCode, result)
        return result

    moves = state.get_best_moves()
    best_move = moves[0]

    for m in moves:
        state.play_move(m, state.current_player)
        value, _ = alphabeta(state, -beta, -alpha, tt, zobrist)
        value = -value
        if value > alpha:
            alpha = value
            best_move = m
        state.undo_move(m)
        if value >= beta:
            result = beta, m
            saveResult(tt, hashCode, result)
            return result

    result = alpha, best_move
    saveResult(tt, hashCode, result)
    return result


# initial call with full window
def call_alphabeta(state, tt, zobrist):
    return alphabeta(state, -INFINITY, INFINITY, tt, zobrist)


def saveResult(tt, cell, loc):
    tt.save(cell, loc)
    return loc

