#Scott Hackett Module 1.3 Assignment

#define the bottle counting function to run the looped text
def countdown_bottles(num_bottles):
    while num_bottles > 1:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        num_bottles -= 1
        bottle_word = 'bottles' if num_bottles > 1 else 'bottle'
        print(f"Take one down and pass it around, {num_bottles} {bottle_word} of beer on the wall.\n")
    
    # When only one bottle is left
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take it down and pass it around, no more bottles of beer on the wall.\n")

def main():
    # Get input for number of bottles and generate text for one and no bottles
    try:
        num_bottles = int(input("Enter number of bottles: "))
        if num_bottles < 1:
            print("Please enter a positive number.")
        else:
            countdown_bottles(num_bottles)
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 100 bottles of beer on the wall.")
    except ValueError:
        print("Please enter a valid number.")

# Start the program
if __name__ == "__main__":
    main()