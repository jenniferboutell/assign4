# Jennifer Boutell
# This program calculates the Armstrong numbers between 10 and a user selected number less than or
# equal to 100,000,000, and prints each one on a new line. It then states how many Armstrong numbers it found.


def get_user_input():
    number = input("Please enter an integer from 10 through 100,000,000 (without the commas):")

    def calculate_armstrong_numbers():
        start = 10
        armstrongs = []
        print("The Armstrong numbers from " + str(start) + " through " + str(number) + " are: ")
        print("")
        for i in range(start, int(number)):
            power = len(str(i))
            total = sum(int(digit)**power for digit in str(i))
            if total == i:
                print(i)
                armstrongs.append(i)
        print("")
        print("The total number of Armstrong numbers found was " + str(len(armstrongs)))
    if int(number) < 10 or int(number) > 100000000:
        print("Error.")
        get_user_input()
    else:
        calculate_armstrong_numbers()


print("Welcome to the Armstrong number calculator.")
get_user_input()
