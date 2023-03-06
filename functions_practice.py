def greeting():
    print("Hello User!")

greeting()

def pack(arg1, arg2, arg3):
     return[arg1, arg2, arg3]

def eat_lunch(my_lunch):
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print(f"First I ate {my_lunch[food_index]}")
        elif food_index < (len(my_lunch) - 1):
            print(f"then I ate {my_lunch[food_index]}")
        else:
            print("My lunchbox is empty!")

greeting()
print(pack(5,34,3))
eat_lunch([])
eat_lunch(["Eggs", "Fish", "Beans"])

