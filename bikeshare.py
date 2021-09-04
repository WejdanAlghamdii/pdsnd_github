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
        try:
            city = input("Would you like to see data for Chicago, New York City, or Washington? ")
            if city.lower() in ['chicago', 'new york city', 'washington']:
                city=city.lower()
                break;
            else:
                print('Wrong input! please choose one of these options: Chicago, New York city, or Washington.')
        except ValueError as ve:
            print('Error Input, please try again!')
            continue

    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month= input('Which month - all, january, february, march, april, may, or june? ')
            if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                month=month.lower()
                break;
            else:
                print('Wrong input! please choose one of these options: all, January, February, March, April, May, June.')
        except ValueError:
            print(' Error Input, please try again!')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day= input('Which day, all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ')
            if day.lower() in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                day=day.lower()
                break;
            else:
                print('Wrong input! please choose one of these options: all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday.')
        except ValueError:
            print(' Error Input, please try again!')
            continue


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is ',common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is ',common_day_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    stations_group = df.groupby(['Start Station','End Station'])
    print('The most frequent combination of start and end stations trip is ',stations_group.size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time = ',total_travel_time)

    # TO DO: display mean travel time
    time_travel_average = df['Trip Duration'].mean()
    print('Average travel time = ',time_travel_average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_counts = df['User Type'].value_counts()
    print('Count of users type: ',users_counts)

    # TO DO: Display counts of gender
    if city == 'washington':
        print('Sorry, there are no gender and year of birth data for Washington city!')
    else:
        gender_counts = df['Gender'].value_counts()

        print('counts based on gender: ',gender_counts)


    # TO DO: Display earliest, most recent, and most common year of birth
        common_birth_year = df['Birth Year'].mode()[0]
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()


        print('The most common year of birth is ',common_birth_year)
        print('The most earliest year of birth is ', earliest_year)
        print('The most recent year of birth is ', recent_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):

    """ Here we ask the user if he\she wants to display raw data or not, the program will continue to display 5 raws till the user type 'no' """

    raw_data = input('Would you like to display some raw data? yes or no? ')


    if raw_data.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            for_more = input('Would you like to display 5 more raw data? yes or no? ')

            if for_more.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
