with open('/Users/bryanlarson/Documents/scripts/adventofcode_2020/5.txt', 'r') as f:
    text = f.read().strip()

# Replace F for easy sorting
passes = text.replace('F', 'A').split('\n')
passes.sort()

seat_ids = []

for p in passes:
    row_l = 0
    row_h = 127
    col_l = 0
    col_h = 7

    for c in p:
        if c == 'A':
            row_h -= (row_h - row_l) / 2 + 1
        if c == 'B':
            row_l += (row_h - row_l) / 2 + 1
        if c == 'L':
            col_h -= (col_h - col_l) / 2 + 1
        if c == 'R':
            col_l += (col_h - col_l) / 2 + 1

    seat_id = row_l * 8 + col_l

    if seat_ids and seat_id - seat_ids[-1] > 1:
        break

    seat_ids.append(seat_id)

print(seat_id - 1)
