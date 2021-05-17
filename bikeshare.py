import time
import pandas as pd
import numpy as np
import calendar
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
info={} # to hold month and day from user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #first loop to hold city
    while True :
        city=input("Choose Country You Want to analyze : chicago \t, new york city\t , washington \t")
        if city not in CITY_DATA :
            print("\nplease input a vaild name for Country you want to analyze its data")
        else:
            break
    print("Ok You want to explore data about {} \n\n".format(city))
    #Second loop to hold month
    while True :
        try:
            month=int(input('''Which month you want to choose. please Enter months as numbers:
 [january=1 , february=2,......May=5] Enter -1 for all months \n\n'''))
        except:
            print("Please Enter a number from 1 to 6 or -1 for all months\n\n")
            continue
        if month not in [-1,1,2,3,4,5,6]:
            print("Please Enter a number from 1 to 6 or -1 for all months\n\n")
        else:
            break
    if month==-1:
        print("Ok you want to explore data for all months\n\n")
    else:
        print("Ok You want to explore data in {} month\n\n".format(calendar.month_name[month]))
    #third loop to hold day
    while True:
        try:
            day=int(input('''Choose a day you want to explore plear Enter days as numbers
monday=0 , tuesday =1 ,.....sunday=6 and Enter -1 for all days of week \n\n'''))
        except:
           print("Please Enter number from 0 to 6 or -1 for all days of week\n\n")
           continue
        if day not in [-1,0,1,2,3,4,5,6]:
            print("Please Enter number from 0 to 6 or -1 for all days of week\n\n")
        else:
            break
    if day==-1 :
        print("Ok you Want to explore data for all days of week\n\n")
    else:
        print("Ok You want to explore data for {}\n\n".format(calendar.day_name[day]))

    info["month"]=month
    info["day"]=day
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
    df=pd.read_csv(CITY_DATA[city])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month"]=df["Start Time"].dt.month #numbers 1 to 6
    df["day_of_week"]=df["Start Time"].dt.weekday # numbers 0(monday) to 6 (sunday)

    if month!=-1:
        df=df[df["month"]==month]
    if day!=-1:
        df=df[df["day_of_week"]==day]
    return df

def special_time_stats(df,month , day):
    if month ==-1:
        common_month=df["month"].mode()[0]
        print("the most Common month : {}".format(calendar.month_name[common_month]))
        if day==-1:
            common_day=df["day_of_week"].mode()[0]
            print("the most common day in this interval : {}".format(calendar.day_name[common_day]))
        else:
            print("These results only for {}s of this interval".format(calendar.day_name[day]))
    else:
        if day==-1:
            print("these results only during {} months".format(calendar.month_name[month]))
            common_day=df["day_of_week"].mode()[0]
            print("the most common day during {} months is {}".format( calendar.month_name[month] ,calendar.day_name[common_day]))
        else:
            print("these results during {} months and {}s of this moths".format(calendar.month_name[month] ,calendar.day_name[day]))

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    special_time_stats(df, info["month"], info["day"])

    # display the most common start hour
    df["hour"]=df["Start Time"].dt.hour
    print("the most common start hour :",df["hour"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station : ( {} ) ".format(df["Start Station"].mode()[0]))


    # display most commonly used end station
    print("Most commonly used end station : ( {} )".format(df["Start Station"].mode()[0]))


    # display most frequent combination of start station and end station trip
    df["Common Trip"]=df["Start Station"]+ "," +df["End Station"]
    common_trip=df["Common Trip"].mode()[0]
    print("the most frequent trip from ( {} ) to ( {} )".format(common_trip.split(",")[0],common_trip.split(",")[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df["Trip Duration"].sum()
    meantime=df["Trip Duration"].mean()
    print("the total travel time is {} seconds equal to {} minutes".format(total_time,total_time/60))
    print("the mean travel time is {} seconds equal to {} minutes".format(meantime, meantime/60))


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\t State Of Users : ")
    dict_user=dict(df["User Type"].value_counts())
    for user_type ,value in dict_user.items():
        print("There are {} {}".format(value,user_type ))


    if city !="washington":
        # Display counts of gender
        print("\t Gender Of Users :")
        dict_gender=dict(df["Gender"].value_counts())
        for user_gender , value in dict_gender.items():
            print("There are {} {}".format(value,user_gender))
        # Display earliest, most recent, and most common year of birth
        print("\t The Dates of Users :")
        print("the earlist date :",df["Birth Year"].max())
        print("the most recent date :",df["Birth Year"].min())
        print("the most common date :",df["Birth Year"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    answer=input("Do you want to see the first 5 rows of data please Enter yes or no ").lower()
    start ,end =0 ,5
    if answer =='yes':
        print(df.iloc[start :end])
        while True:
            answer =input("Do you want to see the next 5 rows please Enter yes or no ").lower()
            if answer=='yes':
                start=end
                end+=5
                print(df.iloc[start:end])
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
