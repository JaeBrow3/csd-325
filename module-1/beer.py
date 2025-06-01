# This program prompts user for the number of bottles beers on the wall,
# and decrements the count until it reaches zero.
def main():

# This function prompts user for the number of bottles of beer on the wall.   
    try:
        bottles = int(input("How many bottles of beer are on the wall: "))
        if bottles < 0:
            print("Number of bottles cannot be negative.")
            return
        
# The loop continues until there are no bottles left and prints the lyrics of 
# the song.
        while bottles > 0:
            print(f"{bottles} bottle{'s' if bottles > 1 else ''} of beer on the wall.")
            print(f"{bottles} bottle{'s' if bottles > 1 else ''} of beer.")
            print("Take one down, pass it around.")
            bottles -= 1
            if bottles == 0:
                print("Time to buy more bottles of beer!")
            else:
                print(f"{bottles} bottle{'s' if bottles > 1 else ''} of beer on the wall.\n")

    except ValueError:
        print("Please enter a integer. Start over!")

if __name__ == "__main__":
    main()