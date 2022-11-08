
try:
    list_user = []

    while True:
        list_user.append(int(input()))

except:
    print('original list =', list_user)

print(list(dict.fromkeys(list_user)))
