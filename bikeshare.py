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
      city = input("Enter the city you would like to explore: ") 
        print(city) 
      if city not in ("Washington", "Chicago", "New York").strip()
        print("City not in data")
        continue
      else:
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      Month = input("Enter the month you would like to explore: ") 
        print(Month) 
      if Month not in ("January", "February", "March", "April", "May", "June", "all").title()
        print("Month not in data")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      Day = input("Enter the day you would like to explore: ") 
        print(day) 
      if day not in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all").title()
        print("Day not in data")
        continue
      else:
        break
    
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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df["month"].mode()[0]
    print("Most common month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_dow=df["day"].mode()[0]
    print("Most common DOW: ", most_common_dow)

    # TO DO: display the most common start hour
    most_common_strt_hr=df["hour"].mode()[0]
    print("Most common start hour: ", most_common_strt_hr)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_strt_station=df["Start Station"].value_counts()
    print("Most common start station: ", most_common_strt_station)
    
    # TO DO: display most commonly used end station
    most_common_end_station=df["End Station"].value_counts()
    print("Most common end station: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["route"]= from df["Start Station"] + df["End Station"]
    most_common_combo=df["route"].mode()[0]
    print("Most common combonation: ", most_common_combo)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df["Trip Duration"])
    print("Total travel time:", Total_Travel_Time/86400, " Days.")

    # TO DO: display mean travel time
    Mean_Travel_Time = df["Trip Duration"].mean()
    print("Mean travel time:", Mean_Travel_Time/60, " Minutes.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_user = df["user type"].value_counts()
    print("User Types: ", type_user)

    # TO DO: Display counts of gender
    gender_types = df["Gender"].value_counts()
    print("Gender Types:", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_by = df["Birth Year"].min()
    print("Earliest Year of Birth:", earliest_by)
    
    most_recent_by = df["Birth Year"].max()
    print("Most Recent Year of Birth:", most_recent_by)
    
    most_common_by = df["Birth Year"].mode()[0]
    print("Most Common Year of Birth:", most_common_by)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        want_raw_data = input("Would you like to see raw data?").strip().lower
        start = 0
        end = 5
        while(want_raw_data == "yes"):
            print(df.iloc[start:end])
            start += 5
            end += 5
            want_raw_data = input("Would you like to see raw data?").strip().lower

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
