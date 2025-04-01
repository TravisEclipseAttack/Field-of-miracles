import random
import time

words = ["олень", "слон", "жираф", "тигр", "лев", "кенгуру", "бегемот", "пантера"]
random_word = random.choice(words)
lives = 3
secretnoe_clovo = ['■'] * len(random_word)

print(" ".join(secretnoe_clovo))
print("Вращайте барабан...")
print(f'У вас {lives} жизни')
time.sleep(1)

def zdox_tochno():
    with open('сдох_точно_100_проц.txt', 'r', encoding='utf-8') as f:
        print(f.read())
def zdox():
    with open('умер.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def pochti_ymer():
    with open('почти_умер.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def shivoy():
    with open('живой.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def search_word(lives, secretnoe_clovo):
    while lives > 0 and '■' in secretnoe_clovo:
        #shivoy()
        sosal = input("350 очков, введите букву или слово целиком: ").lower()

        if len(sosal) > 1:
            if sosal == random_word:
                secretnoe_clovo = list(random_word)
                print(" ".join(secretnoe_clovo))
                print("И у нас есть победитель!")
                return
            else:
                lives -= 1
                print("Вы банкрот!")
                print(f'У вас {lives} жизней')
                zdox()
                if lives == 2:
                    pochti_ymer()
                elif lives == 1:
                    zdox()
                # elif lives == 3:
                #     shivoy()
            continue

        if len(sosal) == 1:
            if sosal in random_word:
                for i in range(len(random_word)):
                    if random_word[i] == sosal:
                        secretnoe_clovo[i] = sosal
                print(" ".join(secretnoe_clovo))
                if lives == 3:
                    shivoy()
                elif lives == 2:
                    pochti_ymer()
            else:
                lives -= 1
                print("Такой буквы нет!")
                print(f'У вас {lives} жизней')
                if lives == 2:
                    pochti_ymer()
                elif lives == 1:
                    zdox()
                elif lives == 0:
                    zdox_tochno()
        else:
            print("Пожалуйста, введите одну букву или слово целиком!")

    if lives == 0:
        print(f"Игра окончена! Загаданное слово было: {random_word}")

def main():
    search_word(lives, secretnoe_clovo)
