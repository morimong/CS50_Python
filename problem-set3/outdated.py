months = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}

while True:
    user_input = input("Input: ")

    if "/" in user_input:
        month, day, year = user_input.split("/")

        if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            print("Invalid date, please enter again.")
            continue

        if len(month) == 1:
            month = "0" + month

        if len(day) == 1:
            day = "0" + day

        print(f"{year}-{month}-{day}")

    elif "," in user_input:
        month_day, year =  user_input.split(",")
        month, day = month_day.split()

        try:

            if month in months:
                month = months[month]

            if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
                print("Invalid date, please enter again.")
                continue

            if len(day) == 1:
                day = "0" + day

            print(f"{year}-{month}-{day}")
        except ValueError:
            print("Invalid, please enter again")