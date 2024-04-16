from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_booking

app = Flask(__name__)



# Get information on availability
@app.route('/availability/<date>')
def get_bookings(date):
    availability = get_all_booking_availability(date)
    return jsonify(availability)


# https://127.0.0.1:5001/availability/2024-04-12

# Add a booking
@app.route('/booking', methods=['POST'])
def add_booking():
    booking = request.get_json()
    class_id = booking.get('class_id')
    time_slot = booking.get('time_slot')
    customer = booking.get('customer')

    if not class_id or not time_slot or not customer:
        return jsonify({'error': 'class_id, time_slot, and customer are required'}), 400

    # Call function to add booking to the database
    booking_id = add_booking(class_id, time_slot, customer)

    if booking_id:
        return jsonify({'booking_id': booking_id}), 201
    else:
        return jsonify({'error': 'Failed to add booking'}), 500


@app.route('/booking', methods=['GET'])
def invalid_method_for_booking():
    return 'Invalid method, use POST'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
