import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

#Define and load dates and temps from csv file
def load_weather_data(filename):
    """Load dates, high and low temperatures from CSV file."""
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # Get dates and high/low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int (row[6])
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

# Plot the high and low temperatures with appropriate colors.
#plt.style.use('seaborn')
def plot_temperatures(dates, temps, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

# Format plot.
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = load_weather_data(filename)

    print("Welcome to the Sitka Weather Program!")
    print("Select an option from the menu:")
    print("1. Highs - Display high temperatures")
    print("2. Lows - Display low temperatures")
    print("3. Exit - Exit the program")
    
    while True:
        # Get user input
        choice = input("\nEnter your choice (1 for Highs, 2 for Lows, 3 for Exit): ")
        
        if choice == '1':
            print("\nDisplaying high temperatures...")
            plot_temperatures(dates, highs, "high", "red")
        elif choice == '2':
            print("\nDisplaying low temperatures...")
            plot_temperatures(dates, lows, "low", "blue")
        elif choice == '3':
            print("\nThank you for using the Sitka Weather Program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()