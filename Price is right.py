import random
p1 = input('Player 1, What is your bid?')
p2 = input('Player 2, What is your bid?')
p3 = input('Player 3, What is your bid?')
p4 = input('Player 4, What is your bid?')
y = random.randint(1000, 5000)
p1 = float(p1)
p2 = float(p2)
p3 = float(p3)
p4 = float(p4)
if p1 == y or p2 == y or p3 == y or p4 == y:
    print('Ding Ding Ding! one player got it exactly right and gets $500!')
if p1>y and p2>y and p3>y and p4>y:
    print('Buzz! Aww... everyone has overbid!')
if p1<y:
    if p1>p2 or p2>y:
        if p1>p3 or p3>y:
            if p1>p4 or p4>y:
                print(f'Actual price is ${y}! Player 1, come on up!')
if p2<y:
    if p2>p1 or p1>y:
        if p2>p3 or p3>y:
            if p2>p4 or p4>y:
                print(f'Actual price is ${y}! Player 2, come on up!')
if p3<y:
    if p3>p1 or p1>y:
        if p3>p2 or p2>y:
            if p3>p4 or p4>y:
                print(f'Actual price is ${y}! Player 3, come on up!')
if p4<y:
    if p4>p1 or p1>y:
        if p4>p2 or p2>y:
            if p4>p3 or p3>y:
                print(f'Actual price is ${y}! Player 4, come on up!')