class Star_Cinema:
    __hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [[0 for x in range(self.__cols)] for x in range(self.__rows)]

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print("Invalid show ID")
            return
        
        for row, col in seat_list:
            if 0 <= row < self.__rows and 0 <= col < self.__cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                    print(f"Seat ({row}, {col}) booked successfully.")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            else:
                print(f"Seat ({row}, {col}) is invalid.")

    def view_show_list(self):
        print("Shows running:")
        for show in self.__show_list:
            print(show)

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show ID")
            return
        seats = self.__seats[id]
        print("Available seats (0 = available, 1 = booked):")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(seats[i][j], end=' ')
            print()



hall1 = Hall(7, 7, 1)
hall1.entry_show('S1', 'Avengers', '10:00')
hall1.entry_show('S2', 'Spiderman', '12:00')
hall1.entry_show('S3', 'Superman', '04:00')
hall1.entry_show('S4', 'Hulk', '08:00')
run = True
while run:
    print("\nOptions: \n")
    print("1: View all Cinema today")
    print("2: View available seats")
    print("3: Book ticket")
    print("4: Exit")
    ch = int(input("\nEnter Option: "))
    if ch == 1:
        hall1.view_show_list()
    elif ch == 2:
        show_id = input("ID: ")
        hall1.view_available_seats(show_id)
    elif ch == 3:
        show_id = input("ID: ")
        rows1 = int(input("Rows: "))
        cols1 = int(input("Cols: "))
        hall1.book_seats(show_id, [(rows1, cols1)])
    elif ch == 4:
        run = False
        print("Exit...")
    else:
        print("Invalid option")