from  datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return (current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return (future_date.strftime("%Y-%m-%d"))

def main():
    current_date = display_current_datetime()
    print(f"Current date and time: {current_date}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date =  calculate_future_date(number_of_days)
    print(f"Future date: {future_date}")

if __name__ == "__main__":
    main()