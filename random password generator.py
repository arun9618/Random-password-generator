import random
letters=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','u','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numbers=('1','2','3','4','5','6','7','8','9','0')
symbols=('!','@','#','$','%','^','&','*','(',')','_','+')
print("welcome to random password generator")
nr_letters=(int(input(f"How many letters you want in your password?\n ")))
nr_numbers=(int(input(f"How many numbers you want in your password?\n ")))
nr_symbols=(int(input(f"How many symblos you want in your password?\n ")))
password_list=[]
for char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_numbers +1):
    password_list += random.choice(numbers)
for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=" "
for char in password_list:
    password+=char
print(f"your password is :{password} ")


