
age = int(input("Enter your age: "))

if age >= 17:
    country = input("Enter your nationality(rwadan,burundian,ugandan,): ")

    if country == "rwandan":
        if age >= 18:
            print("You are eligible to vote in Rwanda.")
        else:
            print("You are not eligible to vote in Rwanda.")

    else:
        if country == "burundian":
            if age >= 20:
                print("You are eligible to vote in Burundi.")
            else:
                print("You are not eligible to vote in Burundi.")

        else:
            if country == "ugandan":
                print("You are eligible to vote in Uganda.")
            else:
                print("Invalid nationality.")

else:
    print("You are not eligible to vote.")
