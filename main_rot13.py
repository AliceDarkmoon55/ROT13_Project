while True:
    t = input()
    list_of_text = ''
    with open('text.txt', 'w') as text:
        text = text.write(t)
    with open('text.txt') as text:
        for line in text:
            list_of_text = list_of_text + line + '\n'

    forward = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    reverse = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    m = 0
    for i in forward:
        n = forward.find(i, m)
        list_t = list_of_text.replace(i, reverse[n])
        m = m + 1
    print('\n' + list_t)
