import requests
import json

def get_availability_by_date(date):
    result = requests.get(
        'http://127.0.0.1:5001/availability/{}'.format(date),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def add_new_booking(date, class_name, time_slot, customer):
    booking = {
        "_date": date,
        "class_name": class_name,
        "time_slot": time_slot,
        "customer": customer
    }
    result = requests.post(
        'http://127.0.0.1:5001/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )
    return result.json()

def display_availability(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
        'Class Name', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
            item['class_name'], item['12-13'], item['13-14'], item['14-15'], item['15-16'], item['16-17'], item['17-18']
        ))

def run():
    print('############################')
    print('Hello, welcome to our fitness class booking system')
    print('############################')
    print()
    date = input('What date would you like to book your class for (YYYY-MM-DD): ')
    print()
    slots = get_availability_by_date(date)
    print('####### AVAILABILITY #######')
    print()
    display_availability(slots)
    print()
    place_booking = input('Would you like to book a class (y/n)?  ')

    book = place_booking.lower() == 'y'

    if book:
        cust = input('Enter your name: ')
        class_name = input('Choose a class (Yoga, Zumba, CrossFit, Pilates): ')
        time_slot = input('Choose a time slot based on availability (e.g., 15-16): ')
        add_new_booking(date, class_name, time_slot, cust)
        print("Booking Successful")
        print()
        slots = get_availability_by_date(date)
        display_availability(slots)

    print()
    print('See you at the class!')

if __name__ == '__main__':
    run()
