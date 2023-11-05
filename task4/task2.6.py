def moves_to_stamp(stamp, target):
    total_stamp_len = len(stamp)
    total_target_len = len(target)
    target = list(target)
    stamped = ['?'] * total_target_len
    moves = []

    def can_stamp_at_position(pos):
        for i in range(total_stamp_len):
            if target[pos + i] != '?' and target[pos + i] != stamp[i]:
                return False
        return True

    def do_stamp_at_position(pos):
        for i in range(total_stamp_len):
            target[pos + i] = '?'
        moves.append(pos)

    made_changes = True
    while made_changes:
        made_changes = False
        for i in range(total_target_len - total_stamp_len + 1):
            if can_stamp_at_position(i) and target[i:i+total_stamp_len] != stamped:
                do_stamp_at_position(i)
                made_changes = True

    if target == stamped:
        return moves[::-1] 
    else:
        return []

