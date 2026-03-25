class BookingManager:
    def __init__(self):
        self.bookings = []

    def book_ticket(self, user, movie_name, showtime, seat):
        booking = {'user': user['username'], 'movie': movie_name, 'showtime': showtime, 'seat': seat}
        self.bookings.append(booking)
        print(f"Booking confirmed: {user['username']} booked {movie_name} at {showtime}, Seat: {seat}")
        self.process_payment(user)

    def show_bookings(self, user):
        print(f"\nBookings for {user['username']}:")
        for booking in self.bookings:
            if booking['user'] == user['username']:
                print(f"{booking['movie']} at {booking['showtime']} - Seat: {booking['seat']}")

    def process_payment(self, user):
        print(f"\nProcessing payment for {user['username']}...")
        payment_method = input("Enter payment method (Credit/Debit): ").strip()
        if payment_method.lower() in ['credit', 'debit']:
            print("Payment successful!")
        else:
            print("Payment failed!")
