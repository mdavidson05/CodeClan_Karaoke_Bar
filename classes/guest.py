class Guest:
    def __init__(self, name, wallet, input_fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = input_fav_song
        self.tab = 0

        # self.age = age
    
    def favourite_song(self, guest):
        if guest.fav_song == self.fav_song:
            print("Wooo!")
            return True
        else:
            return False
        
    def order_drink(self, drink):
        self.tab += drink.price
        return self.tab
