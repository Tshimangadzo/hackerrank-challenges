
def create_alphabets():
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    return alphabet


def join_row(results):
    return "-".join(results)


def split_row(results):
    return results.split()


def get_expected_alphabets(size):
    return create_alphabets()[:size]


def create_arr(string):
    return [x for x in string]


def create_row(size):
    expected_alphabets = get_expected_alphabets(size).copy()
    row = join_row(expected_alphabets)
    print(row)
    expected_alphabets.reverse()
    row = join_row(expected_alphabets)+row[1:len(row)]
    return row


def solve_rangoli(row, index):
    new_index = int(len(row)/2)-index
    row = create_arr(row)
    for i in range(new_index+1):
        row[i] = '-'
        row[i+int(len(row)/2)+index] = '-'
    return row


def get_list(size):
    row_join = create_row(size)
    list_ = []
    for i in range(len(row_join)+1):
        list_.append(solve_rangoli(row_join, i+1))
        if i == int(len(row_join)/2):
            break
    return list_


def remove_unwanted_rows(list_):
    next_list = []
    for index in range(len(list_)):
        if index+1 != len(list_) and list_[index] == list_[index+1]:
            next_list.append(list_[index])
    next_list.append(list_[len(list_)-1])
    return next_list

def print_list(arr):
    for row in arr:
        for col in row:
            print(col, end="")
        print("")

def print_rangoli(size):
    arr = get_list(size)
    arr = remove_unwanted_rows(arr)
    print_list(arr)
    arr.reverse()
    print_list(arr)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
