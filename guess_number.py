from random import randint
WELCOME_TEXT = 'Угадайте число от 1 до 100'
number = randint(1, 100)
print(WELCOME_TEXT)

def main():
    while True:
        guess = int(input('Введите число: '))
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        if guess > number:
            print('Ваше число больше того, что загадано.')
        if guess == number:
            break


main()

print('Отличная интуиция! Вы угадали число :)')
