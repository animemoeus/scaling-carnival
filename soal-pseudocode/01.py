for i in range(50, 101, 5):
    if i <= 60:
        print(f'{i} KURANG')
    elif i > 60 and i <= 70:
        print(f'{i} CUKUP')
    elif i > 70 and i <= 80:
        print(f'{i} BAIK')
    elif i > 80:
        print(f'{i} LUAR BIASA')