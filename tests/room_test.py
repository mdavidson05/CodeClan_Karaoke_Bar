import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.bar import Bar

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Julio", 20, "Hurt")
        self.song = Song("Poker Face")
        self.room = Room("Ben Nevis", 8, 100)
        self.bar = Bar("Jack Daniels", 1.50)

    def test_check_guest_name(self):
        self.assertEqual("Julio", self.guest.name)

    def test_check_song_name(self):
        self.assertEqual("Poker Face", self.song.name)

    def test_check_room_name(self):
        self.assertEqual("Ben Nevis", self.room.name)

    def test_check_guest_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_check_guest_on(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.song))

    def test_check_money(self):
        self.assertEqual(True, self.room.check_money(self.guest.wallet))

    def test_charge_customer(self):
        #print(self.room.till)
        self.room.charge_customer(self.room.entrance_fee, self.guest)
        #print(self.room.till)
        self.assertEqual(108, self.room.till)
        #print(self.guest.wallet)

    # this is actually add a person to a room
    # def test_check_space(self):
    #     self.assertEqual(True, self.room.check_space(self.room.spaces))
    #     print(self.room.spaces)

    def test_full_scenario(self):
        self.room.check_in(self.guest)
        self.room.charge_customer(self.room.entrance_fee, self.guest)
        self.room.add_song(self.song)
        self.guest.order_drink(self.bar)
        print(self.room.till)