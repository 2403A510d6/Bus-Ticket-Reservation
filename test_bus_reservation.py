
from bus_reservation import BusReservation


def test_initial_seats():
    bus = BusReservation("Express", 40, 500)
    assert bus.available_seats() == 40


def test_successful_booking():
    bus = BusReservation("Express", 40, 500)
    booking = bus.book_ticket("Rahul")
    assert booking == 1
    assert bus.available_seats() == 39


def test_cancel_booking():
    bus = BusReservation("Express", 40, 500)
    booking = bus.book_ticket("Rahul")
    result = bus.cancel_ticket(booking)
    assert result == "Booking cancelled successfully"


def test_invalid_booking():
    bus = BusReservation("Express", 40, 500)
    assert bus.book_ticket("") == "Invalid passenger name"


def test_no_seats_available():
    bus = BusReservation("Express", 1, 500)
    bus.book_ticket("Rahul")
    assert bus.book_ticket("Arjun") == "No seats available"


def test_invalid_cancellation():
    bus = BusReservation("Express", 40, 500)
    assert bus.cancel_ticket(99) == "Invalid booking ID"
