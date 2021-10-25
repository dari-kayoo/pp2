moneyOfAzamat = int(input())
moneyOfDauren = int(input())
year = 0
while moneyOfAzamat < moneyOfDauren:
    moneyOfAzamat*=3
    moneyOfDauren*=2
    year+=1
print(year)    