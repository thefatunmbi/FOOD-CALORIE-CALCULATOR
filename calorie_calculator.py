def main():

    print("-----------Food calorie calculator-----------")
    print("Enter a food and its weight to calculate calories")


    food = input("Food: ").lower()
    calories_per_100g = get_calories(food)

    if calories_per_100g is None:
        return

    weight = float(input("Weight(g): " ))

    total_calories = (calories_per_100g / 100) * weight

    print("Food:", food)
    print("Weight:", weight)
    print("Total calories", total_calories)



def get_calories(food):
    if food == "rice":
        calories_per_100g = 123
    elif food == "yam":
        calories_per_100g = 90
    elif food == "potato":
        calories_per_100g = 90
    elif food == "plantain":
        calories_per_100g = 120
    elif food == "egg":
        calories_per_100g = 160
    elif food == "chicken":
        calories_per_100g= 175
    elif food == "beans":
        calories_per_100g = 130
    elif food == "garri":
        calories_per_100g = 360
    elif food == "bread":
        calories_per_100g = 270
    elif food == "beef":
        calories_per_100g = 250
    else:
        print("Enter a valid food!")
        return None
    return calories_per_100g
    

main()

    



