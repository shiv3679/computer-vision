#!/usr/bin/env python3

''' 
Assignment 1 - Version A - Group 1
Section: OPS445NDD
Group Members: Erdinc Eren
               Emmanuel Amo-Ntori 
               Anish
               Jonathan Hyppolite 
               Iain Keeble 
               Manvir Kaur 
               Yuvraj Dhiman 
'''       

# Function to check if the given year is a leap year
def leap_year(year):
    # A year is a leap year if it is divisible 4 but not by 100, except if it is also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    # Otherwise, it is not a leap year
    return False

# Function to return the maximum days in a month, accounting for leap years
def mon_max(year, month):
    # Define days in each month, with index 0 ignored for direct month indexing (1 = January, etc.) 
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # If it's February and a leap year, return 29 days instead of 28
    if month == 2 and leap_year(year):
        return 29
    # Otherwise, return the default days for the given month
    return days_in_month[month]

# Function to calculate the next date given a specific date
def after(date):
    # Extract year, month and day from the date string
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    
    day += 1 # Increment the day to get the next date

    if day > mon_max(year, month):   # Check if the new day exceeds the maximum for the month
        day = 1  # Reset day to 1 if it exceeds month's limit
        month += 1 # Move to the next month

        # Check if month exceeds December (12), and increment the year if so
        if month > 12:
            month = 1  # Reset month to January
            year += 1  # Increment the year

# Function to validate a date and ensure it's within a specified range and format (DD/MM/YYYY)
def valid_date(date):

    # Will validate the user provided date and ensures its in the correct range and format (DD/MM/YYYY)

    try:
        year, month, day = map(int, date.split('/'))  # Parse the date components

        # Check for valid year range (1538-2999)
        if not (1538 <= year <= 2999):
            print("Error: Invalid year. Please enter a year between 1538 and 2999.")
            return None

        # Check for valid month range (1-12)
        if not (1 <= month <= 12):
                print("Error: Invalid month. Please enter a month between 1 and 12.")
                return None
        
        # Check if valid day is within the month's maximum
        if not (1 <= day <= mon_max(year, month)):
                print(f"Error: Invalid day for month {month}. Please enter a day between 1 and {mon_max(year, month)}.")

        # Format and return the validated date as YYYY-MM-DD
        return f"{year:04d}-{month:02d}-{day:02d}"
        
    except ValueError:
            # Handle cases where date input is incorrectly formatted
            print("Error: Invalid date format. Please enter a date in DD/MM/YYYY format.")
            return None