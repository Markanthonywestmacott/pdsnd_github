import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['january', 
              'february', 
              'march', 
              'april', 
              'may', 
              'june', 
              'all']

DAYS_DATA = ['monday', 
             'tuesday', 
             'wednesday', 
             'thursday', 
             'friday', 
             'saturday', 
             'sunday']

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
    city = input("What city would you like to see?").lower()
    
    while city not in ['chicago', 'washington', 'new york city']:
        city = input("We dont have that city").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("please choose a month").lower()
    while month not in MONTH_DATA:
        print("please check your spelling")
        month = input("please choose a month").lower()
    print("retrieving data from: ", month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please choose a day").lower()
    while day not in DAYS_DATA:
        print("please check your spelling")
        month = input("please choose a day").lower()
    print("retrieving data from: ", day)

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
    # TO DO: load the data
    df = pd.read_csv(CITY_DATA[city])
    
    # TO DO (new): filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]          
        
    # TO DO: filter by day
    if day != 'all':
        
        df = df[df['day_of_week'] == day]
    
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("most common month: {}".format(str(df['month'].mode()[0])))

    # TO DO: display the most common day of week
    print("most common day of the week: {}".format(str(df['day_of_week'].mode()[0])))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("most common starting time: {}".format(str(df['start_hour'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_st = df['start_station'].mode().to_string(index = False)
    end_st = df['end_station'].mode().to_string(index = False)
          
    # TO DO: display most commonly used start station
    print('the main starting point is {}:'.format(start_st))

    # TO DO: display most commonly used end station
    print('the main ending point is {}:'.format(ending_st))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['start_station'].str.cat(df['end_station'], sep=' to ')
    value = df['route'].mode().to_string(index = False)
    print('Most popular route is {}:'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time is: {}".format(str(df['duration'].sum()))

    # TO DO: display mean travel time
    print("mean time is: {}".format(str(df['duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO (NEW): Display counts of user types
    subscriber = (df['User Type'] == 'Subscriber')sum()
    customer = (df['User Type'] == 'Customer')sum()
    print("the number of  of users are: {}".format(subscriber,customer))
    
    count = df['User Type'].value_counts()
    print(count)

    # TO DO (NEW): Display counts of gender
    male = (df['Gender'] == 'Male').sum()
    female = (df['Gender'] == 'Female').sum()
    print("the number of males is {} and of females is {}".format(male,female))
          
    
    # TO DO (NEW): Display earliest, most recent, and most common yob
    birth_early = int(df['Birth Year'].min())
    birth_recent = int(df['Birth Year'].max())
    birth_common = int(df['Birth Year'].mode())
    print('earliest birth year: {}'.format(birth_early))
    print('latest birth year: {}'.format(birth_recent))
    print('most common birth year: {}'.format(birth_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df)
    
    # TO DO: display 5 rows as per user request
    first = 0
    last = 5
    answer = ''    
    while answer.lower() not in ['yes', 'no']:
          answer = input("would you like to see all the data?").lower()
          
          if answer.lower() not in ['yes', 'no']:
            print('please check spelling')
          elif answer.lower() == "yes":
            print(df.iloc[first:last])
          
            while True:
                answer_ii = input("would you like to see more data?")
                if answer_ii.lower() not in ['yes', 'no']:
                    print('please check spelling')
                elif answer_ii.lower() == "yes":
                    first += 5
                    last += 5
                    print(df.iloc[first:last])
                elif answer_ii.lower() == "no":
                    break
          elif answer.lower() == "no":
            break
          
          
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
