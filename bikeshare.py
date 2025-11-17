import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid city name. Try again.")
        

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month (january, february, march, april, may, june) or 'all': ").lower()
        if month in months:
            break
        print("Invalid month. Try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day (monday, tuesday, wednesday, thursday, friday, saturday, sunday) or 'all': ").lower()
        if day in days:
            break
        print("Invalid day. Try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    if not df['month'].mode().empty:
        print("Most common month:", df['month'].mode()[0])
    else:
        print("Most common month: No data available (empty mode).")

    # TO DO: display the most common day of week
    if not df['day_of_week'].mode().empty:
        print("Most common day:", df['day_of_week'].mode()[0])
    else:
        print("Most common day: No data available.")


    # TO DO: display the most common start hour
    if not df['hour'].mode().empty:
        print("Most common hour:", df['hour'].mode()[0])
    else:
        print("Most common hour: No data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if not df['Start Station'].mode().empty:
        print("Most common start station:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    if not df['End Station'].mode().empty:
        print("Most common end station:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " → " + df['End Station']
    if not df['trip'].mode().empty:
        print("Most common trip:", df['trip'].mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types:\n", df['User Type'].value_counts(), "\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Gender:\n", df['Gender'].value_counts(), "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest birth year:", int(df['Birth Year'].min()))
        print("Most recent birth year:", int(df['Birth Year'].max()))
        print("Most common birth year:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
def display_data(df):
    """Displays 5 rows of raw data at a time upon user request."""
    
    start_loc = 0
    while True:
        view_data = input("\nDo you want to see 5 rows of raw data? Enter yes or no: ").lower()
        
        if view_data != "yes":
            break

        # Display next 5 rows
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5

        # Stop if no more rows
        if start_loc >= len(df):
            print("\nNo more data to display.")
            break    
  


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
