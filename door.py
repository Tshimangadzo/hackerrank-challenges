
def check_odd_n_natural_number(n):
    if n % 2 == 0:
        raise ValueError("N is not odd number")


def check_n_three_times_m(N, M):
    if 3*N != M:
        raise ValueError("M is not 3 times N")


def raise_errors(N, M):
    check_odd_n_natural_number(N)
    check_n_three_times_m(N, M)


def create_2d_array(N, M):
    arr = []
    for _ in range(int(N/2)):
        new_arr = []
        for _ in range(int(M/2)-1):
            new_arr.append('-')
        arr.append(new_arr)
    return arr


def write_welcome(row, M):
    welcome = ['W', 'E', 'L', 'C', 'O', 'M', 'E']
    copy_row = row[0].copy()
    for v in range(M):
        if v > int(M/2)-4 and len(welcome) > 0:
            copy_row[v] = welcome[0]
            del welcome[0]
    return copy_row


def pop_and_join(row, size):
    copy_list = row.copy()
    if size == 0:
        return copy_list

    for _ in range(size*3):
        copy_list.pop()
    append_str = '.|.'
    for _ in range(size):
        for str_ in append_str:
            copy_list.append(str_)
    return copy_list


def append_center(arr):
    append_str = '.|.'
    length_first = len(arr[0])+3
    for rows in range(len(arr)):
        center = int(length_first/2)-1
        for a in append_str:
            arr[rows].insert(center, a)
            center += 1
    return arr


def modify_arr(arr):
    new_row = []
    for row_numer in range(len(arr)):
        poped_and_joined = pop_and_join(arr[row_numer], row_numer)
        new_row.append(poped_and_joined)
    return new_row


def append_cols(arr):
    save_cols = []
    for rows in arr:
        new_row = rows.copy()
        rows.reverse()
        new_row += rows.copy()
        save_cols.append(new_row)
    return save_cols


def print_board(arr):
    for row in arr:
        for col in row:
            print(col, end="")
        print("")


if __name__ == '__main__':
    input = input().split(" ")
    N, M = int(input[0]), int(input[1])
    raise_errors(N, M)
    arr = create_2d_array(N, M)
    modified_arr = modify_arr(arr)
    saved = append_cols(modified_arr)
    s = append_center(saved)
    print_board(s)
    print("".join(write_welcome(s, M)))
    saved.reverse()
    print_board(saved)