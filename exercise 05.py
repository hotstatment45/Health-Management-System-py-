
#Health Management System


# a=getdate()
# print(a)
# Total 6 files
# write a function when executed takes as input client name[]  chicken roti
# seated shoulder press , [] cable crossover
# One more function to retrieve exercise or food for any client
# 3 clients - Harry, Rohan and Hammad




'''


def getdate():
    import datetime
    return  datetime.datetime.now()

print("====Welcome to the health Management=====")
print("Harry = 1")
print("cold = 2")
print("Hot = 3")

while True:
    user = int(input("Enter value in num: "))

    # harry----
    if user == 1:
        f = open("user1_harry.txt", "w+")
        user_eat = input("what you eaten?: ")
        user_exercise = input("Which exercise you done today? ")
        print("file was created")
        f.write(f"==== User_name:  Harry  ====\n Time: {getdate()}\n Food : {user_eat} \n Workout : {user_exercise} ")
        print(list)
        user_look = input("Great!! file was created. Do you want to take a look??(yes/no):  ").lower()
        # quite=input("Want to quite?(Q) ").lower

        if user_look == "yes":
            f.seek(0)
            read = f.readlines()
            print(read)

        else:
            print("okay, Keep it up!!")



    # cold----------
    if user == 2:
        f = open("user2_cold .txt", "w+")
        user_eat = input("what you eaten?: ")
        user_exercise = input("Which exercise you done today? ")
        print("file was created")

        f.write(f"==== User_name:  Harry  ====\n Time: {getdate()}\n Food : {user_eat} \n Workout : {user_exercise} ")
        print(list)
        user_look = input("Great!! file was created. Do you want to take a look??(yes/no):  ").lower()
        # quite = input("Want to quite?(Q) ").lower
        if user_look == "yes":
            f.seek(0)  # Move the file pointer to the beginning
            read = f.readlines()
            print(read)
        else:
            print("okay, Keep it up!!")
            break



    # Hot------------
    if user == 3:
        f = open("user3_Hot .txt", "w+")
        user_eat = input("what you eaten?: ")
        user_exercise = input("Which exercise you done today? ")
        print("\n file was created")
        f.write(f"==== User_name:  Harry  ====\n Time: {getdate()}\n Food : {user_eat} \n Workout : {user_exercise} ")
        print(list)
        user_look = input("Great!! file was created. Do you want to take a look??(yes/no):  ").lower()
        # quite = input("Want to quite?(Q) ").lower
        if user_look == "yes":
            f.seek(0)  # Move the file pointer to the beginning
            read = f.readlines()
            print(read)
        else:
            print("okay, Keep it up!!")




'''






#Above code convert by    using   function

def getdate():
    import datetime
    return  datetime.datetime.now()

def create_health_record(User_name):
    with open(f"user_{User_name}.txt","w") as f:
        user_exercise=input("which exercise did you do today? ")
        user_eat= input("What did you eat today? ")
        f.write(f"Time: {getdate()}\nName: {User_name}\n Exercise: {user_exercise}\n Food: {user_eat}")
        print("Yea! Data is created.")

def display_health_record(user_name):
    try:
      with open("user_name.txt","r") as f:
          print(f.read())
    except FileNotFoundError:
        print("file isn't created.")


#  user were write
User_name = input("Enter your name: ")
while True:
    print(f"\n\t==-------{User_name}!welcome to Health Management-------==")
    print("1.Create Health Management\n2. Display Health Management\n3. Quite")
    option = int(input("Choose an option: "))

    if option == 1:
        create_health_record(User_name)
    elif option == 2:
        display_health_record(User_name)
    else:
        print("Goodbye!")
        break










