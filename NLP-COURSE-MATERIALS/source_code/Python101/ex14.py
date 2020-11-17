money=int(input('Enter amount of money:'))

a_hundred_banknote=money//100
money=money%100

fifty_banknote=money//50
money=money%50

twenty_banknote=money//20
money=money%20

ten_banknote=money//10
money=money%10

print('# of 100 tl banknotes:',a_hundred_banknote, '\n# of 50 tl  banknotes:',fifty_banknote,'\n# of 20 tl banknotes:',twenty_banknote,'\n# of 10 tl banknotes:',ten_banknote)
print(money,'tl can not be paid')