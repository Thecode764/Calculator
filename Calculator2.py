from colorama import init,Fore
init()
n_1 = int(input(Fore.RED + "Enter First Number:"))
n_2 = int(input(Fore.CYAN + "Enter Second Number:"))
answer1 = n_1 + n_2
answer2 = n_1 - n_2
answer3 = n_1 * n_2
answer4 = n_1 % n_2
answer5 = n_1 / n_2
print("mark+",answer1)
print("mark-",answer2)
print("mark*",answer3)
print("mark%",answer4)
print("mark/",answer5)
