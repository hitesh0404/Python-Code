from users import UserManager
from movies import MovieManager
from bookings import BookingManager
from database import Database

class TicketBookingSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.movie_manager = MovieManager()
        self.booking_manager = BookingManager()
        self.database = Database()

    def run(self):
        while True:
            print("\n--- Welcome to the Movie Ticket Booking System ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break  
            else:
                print("Invalid choice. Please try again.")

    def register_user(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        user = self.user_manager.register(username, password)
        if user:
            print("Registration successful!")

    def login_user(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        user = self.user_manager.login(username, password)
        if user:
            self.user_menu(user)

    def user_menu(self, user):
        while True:
            print("\n--- User Menu ---")
            print("1. View Movies")
            print("2. Select Seat and Book Ticket")
            print("3. Show Bookings")
            print("4. Logout")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.view_movies()
            elif choice == '2':
                self.select_seat_and_book(user)
            elif choice == '3':
                self.booking_manager.show_bookings(user)
            elif choice == '4':
                print("Logging out...")
                break  
            else:
                print("Invalid choice. Please try again.")

    def view_movies(self):
        movies = self.movie_manager.get_movies()
        if movies:
            for idx, movie in enumerate(movies, 1):
                print(f"{idx}. {movie['name']} - Showtimes: {', '.join(movie['showtimes'])}")
        else:
            print("No movies available.")

    def select_seat_and_book(self, user):
        movie_name = input("Enter movie name: ").strip()
        showtime = input("Enter showtime: ").strip()

        movie = next((m for m in self.movie_manager.get_movies() if m['name'] == movie_name), None)
        if movie:
            self.movie_manager.display_seats(movie_name)
            try:
                row = int(input("Enter row number (1-5): ").strip()) - 1
                col = int(input("Enter column number (1-5): ").strip()) - 1
                if self.movie_manager.reserve_seat(movie_name, row, col):
                    self.booking_manager.book_ticket(user, movie_name, showtime, f"Row {row + 1}, Col {col + 1}")
                else:
                    print("Seat is already booked.")
            except ValueError:
                print("Invalid input. Please enter numbers between 1 and 5.")
        else:
            print("Movie not found.")

if __name__ == "__main__":
    
    system = TicketBookingSystem()
    system.movie_manager.add_movie('Avatar 2', ['10:00 AM', '02:00 PM', '06:00 PM'])
    system.movie_manager.add_movie('Iron Man 4', ['11:00 AM', '03:00 PM', '07:00 PM'])

    system.run()
from users import UserManager
from movies import MovieManager
from bookings import BookingManager
from database import Database

class TicketBookingSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.movie_manager = MovieManager()
        self.booking_manager = BookingManager()
        self.database = Database()

    def run(self):
        while True:
            print("\n--- Welcome to the Movie Ticket Booking System ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break  
            else:
                print("Invalid choice. Please try again.")

    def register_user(self):
        while True:
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if username and password:
                user = self.user_manager.register(username, password)
                if user:
                    print("Registration successful!")
                    break
                else:
                    print("Username already exists. Please try again.")
            else:
                print("Username and password cannot be empty.")

    def login_user(self):
        while True:
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if username and password:
                user = self.user_manager.login(username, password)
                if user:
                    self.user_menu(user)
                    break
                else:
                    print("Invalid username or password. Please try again.")
            else:
                print("Username and password cannot be empty.")

    def user_menu(self, user):
        while True:
            print("\n--- User Menu ---")
            print("1. View Movies")
            print("2. Select Seat and Book Ticket")
            print("3. Show Bookings")
            print("4. Logout")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.view_movies()
            elif choice == '2':
                self.select_seat_and_book(user)
            elif choice == '3':
                self.booking_manager.show_bookings(user)
            elif choice == '4':
                print("Logging out...")
                break  
            else:
                print("Invalid choice. Please try again.")

    def view_movies(self):
        movies = self.movie_manager.get_movies()
        if movies:
            for idx, movie in enumerate(movies, 1):
                print(f"{idx}. {movie['name']} - Showtimes: {', '.join(movie['showtimes'])}")
        else:
            print("No movies available.")

    def select_seat_and_book(self, user):
        while True:
            movie_name = input("Enter movie name: ").strip()
            showtime = input("Enter showtime: ").strip()

            movie = next((m for m in self.movie_manager.get_movies() if m['name'] == movie_name), None)
            if movie:
                self.movie_manager.display_seats(movie_name)
                try:
                    row = int(input("Enter row number (1-5): ").strip()) - 1
                    col = int(input("Enter column number (1-5): ").strip()) - 1
                    if row < 0 or row > 4 or col < 0 or col > 4:
                        print("Invalid input. Please enter numbers between 1 and 5.")
                    elif self.movie_manager.reserve_seat(movie_name, row, col):
                        self.booking_manager.book_ticket(user, movie_name, showtime, f"Row {row + 1}, Col {col + 1}")
                        break
                    else:
                        print("Seat is already booked.")
                except ValueError:
                    print("Invalid input. Please enter numbers between 1 and 5.")
            else:
                print("Movie not found.")

if __name__ == "__main__":
    
    system = TicketBookingSystem()
    system.movie_manager.add_movie('Avatar 2', ['10:00 AM', '02:00 PM', '06:00 PM'])
    system.movie_manager.add_movie('Iron Man 4', ['11:00 AM', '03:00 PM', '07:00 PM'])

    system.run()