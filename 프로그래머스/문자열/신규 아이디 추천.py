def solution(new_id):
    new_id = new_id.lower()
    temp = list(x for x in new_id if x.isalpha() or x.isnumeric() or x in ['-', '_', '.'])
    new_id = ''

    for i in range(len(temp)):
        if new_id and new_id[-1] == '.' and temp[i] == '.':
            continue

        new_id += temp[i]

    if new_id[0] == '.' and new_id[-1] == '.':
        new_id = new_id[1:-1]
    elif new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) == 0: new_id = 'a'
    if len(new_id) > 15: new_id = new_id[:15]
    if new_id[-1] == '.': new_id = new_id[:-1]
    if len(new_id) <= 2: new_id = new_id + new_id[-1] * (3 - len(new_id))

    return new_id