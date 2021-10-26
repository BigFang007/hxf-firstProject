# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# name1 = " yang jiarui"
# name2 = "huang xiaofang "
#
# famous_person1 = " lu xun "
# print("hello " + name1.title().lstrip() + ", " + "Would you like to do love with " + name2.title().rstrip() + "?")
# print("hello " + name1.upper().lstrip() + ", " + "Would you like to do love with " + name2.lower().rstrip() + "?")
# message = '"A person who didn\'t like to do love is lower than a dog."'
# print("As " + famous_person1.title().strip() + " has said, \n\t" + message)
# print(3 / 2)
# print(7 + 1)
# print(9.2 + 2.2)
# print(2 ** 3)
# print(16 / 3)
# print("小房子是个大可爱")
# print("丝绸房子怎么不去学习python呀，真是个丝绸房子，再也不喜欢你了")
# abc = "cdf"
# print("abc" + abc)
# a = ["b", "c", "d", '3', "4", 8 + 2, 9]
# print(a)
# print(a.pop())
# print(a)
# print(a[3])
#
# # invite friends
# names = ['yang jiarui', 'su su', 'xiao fangzi']
# print("Dear " + names[0].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[1].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[2].title() + ", Would you like to have dinner with me?")
# not_ok = names.pop()
# print("it's a pity that " + not_ok.title() + " couldn't come.")
# names.append('wang bingbing')
# print("Dear " + names[0].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[1].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[2].title() + ", Would you like to have dinner with me?")
# print("I find a bigger table")
# names.insert(0, 'a')
# names.insert(2, 'b')
# names.append('c')
# print("Dear " + names[0].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[1].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[2].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[3].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[4].title() + ", Would you like to have dinner with me?")
# print("Dear " + names[5].title() + ", Would you like to have dinner with me?")
# print("I'm sorry for the bad table.Only two people can have dinner with me now.")
# names2 = [names.pop(0), names.pop(1), names.pop(-1), names.pop(2)]
# print(names2)
# print(names)
# print("Dear " + names2[0].title() + ", I'm sorry.")
# print("Dear " + names2[1].title() + ", I'm sorry.")
# print("Dear " + names2[2].title() + ", I'm sorry.")
# print("Dear " + names2[3].title() + ", I'm sorry.")
# print("Dear " + names[0].title() + ", welcome!")
# print("Dear " + names[1].title() + ", welcome!")
# del names[0]
# del names[0]
# print(names)


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * x - factorial(x - 1)) / 3


class Light_son:
    def __init__(self, wing, candle):
        self.wing = wing
        self.candle = candle

    def applaud(self):
        print("With " + str(self.wing) + " wings' light son is applauding! ")
