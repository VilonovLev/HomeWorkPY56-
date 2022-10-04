from turtle import pos
from pygame import*

init()

W = 300
H = 300

sc = display.set_mode((W,H))
display.set_caption("TicTacToe")
display.set_icon(image.load('image\\tic-tac-toe-512.webp'))
x_im = transform.scale((image.load('image\\x.png')),(W//3,W//3))
o_im = transform.scale((image.load('image\\o.png')),(W//3,W//3))
field_im = transform.scale((image.load('image\\field.webp')),(W,H))
field = [["1","2","3"],
         ["4","5","6"],
         ["7","8","9"]]

def win(fld):
    for i in range(3):
        if [fld[i][0]] == [fld[i][1]] == [fld[i][2]]:
            return True
        elif [fld[0][i]] == [fld[1][i]] == [fld[2][i]]:
            return True
    if [fld[0][0]] == [fld[1][1]] == [fld[2][2]]:
        return True
    elif [fld[0][2]] == [fld[1][1]] == [fld[2][0]]:
        return True
    return False

FPS = 60
clock = time.Clock()

sc.blit(field_im,(0,0))
display.update()
turn = 0
while True:
    for even in event.get():
        if even.type == QUIT:
            exit()
        elif even.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            if field[pos[0]//100][pos[1]//100].isdigit():
                if turn%2==0:
                    sim = x_im
                    field[pos[0]//100][pos[1]//100] = "x"
                else:
                    sim = o_im
                    field[pos[0]//100][pos[1]//100] = "o"
                turn += 1
                sc.blit(sim,(pos[0] - pos[0]%100,pos[1] - pos[1]%100))
                if win(field):
                    sc.fill((255, 255, 0))
                    text = f"Победил!"
                    font = font.Font(None, 30)
                    text = font.render(text, True, (0,0,0))
                    sc.blit(text, (100, 70))
                    sc.blit(sim,(100,130))
                if turn > 8:
                    sc.fill((150, 150, 150))
                    text = f"Ничья!"
                    font = font.Font(None, 30)
                    text = font.render(text, True, (0,0,0))
                    sc.blit(text, (120, 120))
        display.update()
    clock.tick(FPS)

# 3. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением.
#  Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dict(args):
    return {x:x for x in args} 

print(to_dict([1,2,3,55]))

# 4. Иван решил создать самый большой словарь в мире. 
# Для этого он придумал функцию biggest_dict(**kwargs), которая принимает неограниченное количество 
# параметров «ключ: значение» и обновляет созданный им словарь my_dict, 
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kargs):
    for i,j in kargs.items():
        my_dict[i] = j
    return my_dict

print(biggest_dict(lina = 2,igor = 4,fedor = 2))
print(biggest_dict(zina = 2,rita = 4,kir = 2))

# 5. Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа
#  (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся 
# последовательности. Для построения словаря создайте функцию count_it(sequence), 
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

def count_it(sequence):
    new_dict = {}
    for num in sequence:
        if num not in new_dict.keys():
            new_dict[num] = 0
        new_dict[num] += 1
    return new_dict

print(count_it(input()))