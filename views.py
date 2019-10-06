from peewee import *
from database import Artwork, Artist
import main
'''
class addArtist(Model):
    def add_new_artsit(self):
        artistName = input('Please enter an artist name: ')
        artistEmail = input('Please enter the artist email: ')
        newArtist = Artist(name = artistName, email = artistEmail)
        newArtist.save()

class allArtForArtist(Model):
    def all_art_for_artist():
        artistSearch = input('Which Artist\'s work would you like to search? ')
        findArtwork = Artwork.select().where(Artwork.artist == artistSearch)
        for art in findArtwork:
            print(art)

class allAvailableArtwork(Model):
    def available_artwork():
        artistSearch = input('Which Artist\'s Available artwork would you like to search? ')
        findAvailable = Artwork.select().where(Artwork.artist == artistSearch and Artwork.availability == 'Available')
        for art in findAvailable:
            print(art)

class addNewArtwork(Model):
    def add_new_artwork():
        newArtArtist = input('Please enter this artworks artist: ')
        artworkName = input('Please enter the artworks name: ')
        newPrice = int(input('Please enter the artworks price: '))
        newAvailability = input('IS this artwork Available or Sold? ')
        newArtwork = Artwork(artist = newArtArtist, artwork = artworkName, price = newPrice, availability = newAvailability)
        newArtwork.save()

class deleteArtwork(Model):
    def delete_artwork():
        artworkSearch = input('What artwork would you like to delete? ')
        artworkDeleted = Artwork.delete().where(Artwork.artwork == artworkSearch)
        print('Artwork Deleted: ', artworkDeleted)

class changeAvailability(Model):
    def change_availability():
        artworkSearch = input('What artwork would you like to change the availability on? ')
        newAvailability = input('Is this artwork Available or Sold? ')
        availabilityChanged = Artwork.update(availability = newAvailability).where(Artwork.artwork == artworkSearch).execute()
        print('The following availability has been changed', availabilityChanged)