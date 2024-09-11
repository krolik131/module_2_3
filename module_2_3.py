my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_spiska = 0
while index_spiska < len(my_list):
    if my_list[index_spiska] < 0:
        break
    else:
        if my_list[index_spiska] == 0:
            index_spiska += 1
            continue
        print(my_list[index_spiska])
        index_spiska += 1
