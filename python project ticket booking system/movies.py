class MovieManager:
    def __init__(self):
        self.movies = []
        self.seats = {}

    def add_movie(self, name, showtimes):
        movie = {'name': name, 'showtimes': showtimes}
        self.movies.append(movie)
        self.seats[name] = [['Available'] * 5 for _ in range(5)]  

    def get_movies(self):
        return self.movies

    def display_seats(self, movie_name):
        seats = self.seats.get(movie_name)
        if seats:
            print("Seat Map for", movie_name)
            for i, row in enumerate(seats, start=1):
                print(f"Row {i}: " + " ".join(row))
        else:
            print("No seats available for this movie.")

    def reserve_seat(self, movie_name, row, col):
        if self.seats[movie_name][row][col] == 'Available':
            self.seats[movie_name][row][col] = 'Booked'
            return True
        return False
