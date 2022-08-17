run = True
while run:
    user_input = int(input('Enter Number: '))
    if user_input == 7:
        print('You won!')
        run = False
    else:
        print('try again!')
        continue
# how many attempt left
attempt = 5
for i in range(5):
    user_input = int(input('Enter Number: '))

    if user_input == 7:
        print('You won!')
        break
    else:
        print(f'Try again! {attempt} left.')
        attempt -= 1
        continue

