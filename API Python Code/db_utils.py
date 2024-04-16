import mysql.connector
from config import HOST, USER, PASSWORD
from pprint import pprint

class DBConnectionError(Exception):
    pass
def _connect_to_db(db_name: str):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection


def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'class_name': item[0],
            '12-13': 'Not Available' if item[1] else 'Available',
            '13-14': 'Not Available' if item[2] else 'Available',
            '14-15': 'Not Available' if item[3] else 'Available',
            '15-16': 'Not Available' if item[4] else 'Available',
            '16-17': 'Not Available' if item[5] else 'Available',
            '17-18': 'Not Available' if item[6] else 'Available',
        })
    return mapped


def get_all_booking_availability(_date):
    try:
        db_name = 'fitness_class'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        print("Connected to DB success")
        availability = []
        query = """
        SELECT class_name, `12-13`, `13-14`, `14-15`, `15-16`, `16-17`, `17-18`
        FROM class_bookings
        WHERE booking_date = '{}';
        """.format(_date)

        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        availability = _map_values(results)
    except Exception:
        raise DBConnectionError("Failed to read from database")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

    return availability


def add_booking(_date, class_name, time_slot, customer):
    try:
        db_name = 'fitness_class'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        print("Connected to DB success")
        query = """
        UPDATE class_bookings
        SET 
            `{}` = 1,
            `{}-booking-id` = '{}'
        WHERE 
            booking_date = '{}' AND class_name = '{}';
        """.format(time_slot, time_slot, customer, _date, class_name)

        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        print("New record updated")
    except Exception:
        raise DBConnectionError("Failed to update database")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")
