from multiprocessing.context import SpawnProcess


class Room:
    def __init__(self, name, spaces, till):
        self.name = name
        self.spaces = spaces
        self.till = till
        self.entrance_fee = 8
        self.guests = []
        self.song = []

    def check_in(self, guest):
        self.guests.append(guest)
        return self.guests

    def check_out(self, guest):
        self.guests.remove(guest)
        return self.guests

    def add_song(self, song):
        self.song.append(song)
        return self.song

    def check_money(self, money):
        if money >= self.entrance_fee:
            return True
        else:
            print("There's an ATM round the corner")
            return False

    def charge_customer(self, entrance_fee, guest):
        if entrance_fee >= self.entrance_fee:
            self.till += self.entrance_fee
            guest.wallet -= self.entrance_fee
            return self.till
    

        
        #This is add a person to a room
    # def check_space(self, space):
    #     if space > 0:
    #         self.spaces -= 1
    #         print(self.spaces)
    #         return True
    #     else:
    #         print("There's no space m8")