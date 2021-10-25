your_full_id = input("Type your full ID : ")
last_two_int = int(your_full_id[len(your_full_id) - 2:]) % 30
if last_two_int != 0 and last_two_int != 30:
    print(f'Your variant : {last_two_int}')
else: print(f'Your variant : {30}')