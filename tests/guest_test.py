import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.bar import Bar

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Julio", 20, "Poker Face")
        self.song = Song("Poker Face")
        self.room = Room("Ben Nevis", 8, 100)
        self.bar = Bar("Jack Daniels", 1.50)

    def test_favourite_song(self):
        self.assertEqual(True, self.guest.favourite_song(self.guest))

    def test_order_drink(self):
        self.assertEqual(1.50, self.guest.order_drink(self.bar))
        


