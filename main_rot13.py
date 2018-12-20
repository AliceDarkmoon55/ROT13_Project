while True:
    t = input()
    with open('text.txt', 'w') as text:
        text = text.write(t)
    with open('text.txt') as text:
        list_of_text = text.readlines()
    forward = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    reverse = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    m = 0
    for k in list_of_text:
        for i in forward:
            n = forward.find(i, m)
            list_of_text = list_of_text.replace(i, reverse[n])
            m = m + 1
    print(list_of_text)
