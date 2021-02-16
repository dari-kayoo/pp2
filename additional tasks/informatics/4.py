pi_list = list()
pi1 = 4
pi2 = 1
for i in range(10):
    pi3 = (pi1 / pi2)
    pi_list.append(pi3)
    pi2 += 2
pi = float(pi_list[0] - pi_list[1] + pi_list[2] - pi_list[3] + pi_list[4] - pi_list[5] + pi_list[6] - pi_list[7] + pi_list[8] - pi_list[9])
 
print(pi)