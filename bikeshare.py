import time
import math
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please select your city from: \n-washington \n-chicago \n-new york city \n' ).lower()
        city = city.lower()
        if city in cities:
            print('You have selected: \n {}'.format(city))
            break
        else:
            print('Sorry, that is not a valid city. Please try again')
            '''
              Ask user to select city. City can be lower or upper case using the lower Function
              the function will itterate through the cities and return data for the inputed City
              If the city is not in cities this will throw an error and restart the process
            '''


    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Please select month to filter by: \n').lower()
        if month in months:
            print('You have selected: \n {}'.format(month))
            break
        else:
            print('Your selection is not valid. Please try again and remember to check spelling')

            '''
               Ask user to select month. Month can be lower or upper case using the lower Function
               the function will itterate through the months variable and return data for the inputed month
               If the month is not in months this will throw an error and restart the process
            '''

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please select the day you want to filter. \nIf you want no filter, please enter "all" \n').lower()
        if day in days:
            print('You have selected \n {}'.format(day))
            break
        else:
            print('Please try again')
            '''
               Ask user to select day. Day can be lower or upper case using the lower Function
               the function will itterate through the days variable and return data for the inputed day
               If the day is not in days this will throw an error and restart the process
            '''

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month_select = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_select.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def selectstats(df):
    while True:
        filter_stats = input('How would you like to filter:\n 1 - Time Stats\n 2 - User Stats\n 3 - Station Stats\n 4 - Trip Duration Stats \n 5 - All Stats\n' )
        #for stat in filter_stats:
        if filter_stats == '1':
            return time_stats(df)
        if filter_stats == '2':
            return user_stats(df)
        if filter_stats == '3':
            return station_stats(df)
        if filter_stats == '4':
            return trip_duration_stats(df)
        if filter_stats == '5':
            return time_stats(df), user_stats(df), station_stats(df)
        if filter_stats != '1' or '2' or '3' or '4' or '5':
            print('That is not a valid input. Please try again')


    '''
       This filter allows users to see specific statistical data from the program.
       Given a selection on a number value, it returns the assocaited stat Functions
       If the input is outside not available an error is thrown and the function restarted
    '''


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    index_month = int(df['Start Time'].dt.month.mode())
    common_month = months[index_month - 1]
    '''
    finds the mode in the data set and uses -1 to account for zero indexing
    '''
    print('The most common month is:\n {}'.format(common_month))
    print()

    # display the most common day of week

    index_day = int(df['Start Time'].dt.weekday.mode())
    common_day = days[index_day - 1]
    '''
    finds the mode in the data set and uses -1 to account for zero indexing
    '''
    print('The most common day is:\n {}'.format(common_day))
    print()

    # display the most common start hour

    common_hour = df['Start Time'].dt.hour.mode()[0]

    print('The most common start hour is {}:00 hours\n'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly occuring Start Station is: \n {}'.format(common_start_station))
    print()


    common_end_station = df['End Station'].mode()[0]
    print('The most commonly occuring End Station is: \n {}'.format(common_end_station))
    print()

    df["combined"] = df["Start Station"] + " - "+ df["End Station"]
    common_combined = df["combined"].mode()[0]

    print('The most frequent occurence of a start and end station group is \n {}'.format(common_combined))
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_trip = df['Trip Duration'].sum()

    minutes = int(math.floor(total_trip / 60))
    hours = int(math.floor(total_trip / 3600))
    days_calc = int(math.floor(total_trip / 86400))
    years = int(math.floor(total_trip / 31536000))
    print('Trip Duration breakdown is as follows:\n')
    print('Minutes {}:'.format(minutes))
    print('Hours {}:'.format(hours))
    print('Days {}:'.format(days_calc))
    print('Years {}:'.format(years))

    def TimeConvert(num):
        hours = int(math.floor(num / 3600))
        minutes = num % 60

      # combine the hours and minutes

        return str(hours) + ':' + str(minutes)
    print('The total trip was:')
    print(TimeConvert(total_trip))


    '''
    total_trip = df['Trip Duration'].sum()
    hours = int(math.floor(total_trip / 3600))
    minutes = int(math.floor(total_trip % 60))

    print('The total trip travel time has been: \n {} hours and {} minutes:'.format(hours, minutes))
    print()

    calculates the sum of time per city as total seconds
    divides the seconds by 3600 to get hours
    returns the remainder of the seconds in minutes using the modulo function
    an alternate for hours could be integer division
    '''

    # display mean travel time
    mean_trip = df["Trip Duration"].mean()
    mean_trip_minutes = mean_trip // 60
    mean_trip_seconds = mean_trip % 60
    '''
    calculates the sum of time per city as total seconds
    divides the seconds by 60 to get minutes
    returns the remainder of the seconds in seconds using the modulo function
    an alternate for minutes could be using the math.floor function
    '''
    print('The mean travel time is: \n {} minutes and {} seconds'.format(mean_trip_minutes, mean_trip_seconds))
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        users = df['User Type']
        subscriber_count = 0
        customer_count = 0
        unkown_count = 0

        for user in users:
            if user == "Subscriber":
                subscriber_count += 1
            elif user == "Customer":
                customer_count += 1
            elif user not in ("Subscriber", "Customer"):
                unkown_count += 1
        '''
        this function will itterate through the user types in the data set, count the occurence of each variant and update the associate count variable
        on each itteration until no more rows are available.

        The function then returns the totals in a print statement
        The returned data is for Counts of user types
        '''
        print('User volumes are as follows:\n {} subscribers, \n {} customers \n {} empty or unknown values\n'.format(subscriber_count, customer_count, unkown_count))
    except KeyError:
        print('No user type data has been returned')
    print()
    '''
    In the event 'User type' does not exist, the try statement will pass an exception and a message will be printed
    to the user that no user type data exists
    '''

    try:
        genders = df['Gender']
        male_count = 0
        female_count = 0
        unkown_gender_count = 0
        for gender in genders:
            if gender == "Male":
                male_count += 1
            elif gender == "Female":
                female_count += 1
            elif gender not in ("Male", "Female"):
                unkown_count += 1
        print('Male vs. Female gender counts are as follows: \n {} males, \n {} females \n {} empty or unknown gender values\n'.format(male_count, female_count, unkown_gender_count))
        '''
        this function will itterate through the user types in the data set, count the occurence of each variant and update the associate count variable
        on each itteration until no more rows are available
        The function then returns the totals in a print statements
        The returned data is for Gender values
        '''
    except KeyError:
        print('No gender data was returned')
        '''
        In the event 'Gender' does not exist, the try statement will pass an exception and a message will be printed
        to the user that no gender data exists
        '''
    print()
    # Display earliest, most recent, and most common year of birth

    try:
        earliest = df["Birth Year"].min()
        most_recent = df["Birth Year"].max()
        most_common = df["Birth Year"].mode()[0]
        print('The earliest birth year is: \n {}'.format(earliest))
        print()
        print('The most recent birth year is: \n {}'.format(most_recent))
        print()
        print('The most common birth year is: \n {}'.format(most_common))
        print()
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        '''
        The function will find the min, max and mode of birth related data and return them in print statements
        '''
    except KeyError:
        print('No Birth Data returned')
        '''
        If not birth data exists, the try statement will use a keyerror to return a "no birth data" result
        '''

def see_raw(df):
    while True:
        get_raw = input('Would you like to see raw data\n' ).lower()
        if get_raw != 'yes':
            break
        select_lines = input('How  many lines would you like to review?:\n 10 \n 20 \n 50 \n')
        if select_lines == '10':
            print('you have selected the first 10 lines \n')
            print(df.head(10))
        elif select_lines == '20':
            print('you have selected the first 20 lines \n')
            print(df.head(20))
        elif select_lines == '30':
            print('you have selected the first 50 lines \n')
            print(df.head(50))
        elif select_lines != '10' or '20' or '50':
            print('That is an invalid option, please try again')

        restart = input("Would you like restart raw data? yes/no: \n" )
        if restart.lower() != 'yes':
            break

def run_descr(df):
    while True:
        run_now = input('Would you like to see Descriptive statistics for the dataset? yes/no \n')
        if run_now != 'yes':
            break
        else:
            print(df.describe())

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        selectstats(df)
        while True:
            restart = input("Would you like to view more statistical categories? yes/no: \n" )
            if restart.lower() == 'yes':
                selectstats(df)
            else:
                break
        see_raw(df)
        run_descr(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
