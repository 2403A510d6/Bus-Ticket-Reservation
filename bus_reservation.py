
class BusReservation:

    def __init__(self, bus_name, total_seats, price):
        self.bus_name = bus_name
        self.total_seats = total_seats
        self.price = price
        self.bookings = {}

    def available_seats(self):
        return self.total_seats - len(self.bookings)

    def book_ticket(self, passenger_name):
        if not passenger_name.strip():
            return "Invalid passenger name"

        if self.available_seats() <= 0:
            return "No seats available"

        booking_id = len(self.bookings) + 1
        self.bookings[booking_id] = passenger_name
        return booking_id

    def cancel_ticket(self, booking_id):
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return "Booking cancelled successfully"

        return "Invalid booking ID"

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id)
