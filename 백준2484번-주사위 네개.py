def dice_price():
    dice_list = sorted(list(map(int, input().split())))
    if len(set(dice_list)) == 1:
        return 50000 + (dice_list[0] * 5000)
    if len(set(dice_list)) == 2:
        if dice_list[1] == dice_list[2]:
            return 10000 + (dice_list[1] * 1000)
        return 2000 + (dice_list[1] + dice_list[2]) * 500
    for i in range(len(dice_list)-1):
        if dice_list[i] == dice_list[i + 1]:
            return 1000 + (dice_list[i] * 100)
    return dice_list[-1] * 100


n = int(input())

print(max(dice_price() for i in range(n)))
