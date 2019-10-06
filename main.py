from peewee import *
from database import Artwork, Artist
from views import addArtist, allArtForArtist, allAvailableArtwork, addNewArtwork, deleteArtwork, changeAvailability

def main():
    catalogContinue = 'Y'

    while catalogContinue.upper() == 'Y':
        choice = 0
        
        print('Welcome to the National Artist Catalog!')
        print('Here are the things you can do with this catalog.')
        print('1) Add a new artist\n2) Search all artwork of a particular artist')
        print('3) Search all available artwork for an artist\n4) Add a new piece of artwork')
        print('5) Delete a piece of artwork\n6) Change availability off a piece of artwork')
        choice = input('What would you like to do? ')
    
        if choice == 1:
            artistName = input('Please enter an artist name: ')
            artistEmail = input('Please enter the artist email: ')
            newArtist = Artist(name = artistName, email = artistEmail)
            newArtist.save()
            catalogContinue = input('Would you like to continue?(Y or N) ')
        elif choice == 2:
            artistSearch = input('Which Artist\'s work would you like to search? ')
            findArtwork = Artwork.select().where(Artwork.artist == artistSearch)
            for art in findArtwork:
                print(art)
            catalogContinue = input('Would you like to continue?(Y or N) ')
        elif choice == 3:
            artistSearch = input('Which Artist\'s Available artwork would you like to search? ')
            findAvailable = Artwork.select().where(Artwork.artist == artistSearch and Artwork.availability == 'Available')
            for art in findAvailable:
                print(art)
            catalogContinue = input('Would you like to continue?(Y or N) ')
        elif choice == 4:
            newArtArtist = input('Please enter this artworks artist: ')
            artworkName = input('Please enter the artworks name: ')
            newPrice = int(input('Please enter the artworks price: '))
            newAvailability = input('IS this artwork Available or Sold? ')
            newArtwork = Artwork(artist = newArtArtist, artwork = artworkName, price = newPrice, availability = newAvailability)
            newArtwork.save()
            catalogContinue = input('Would you like to continue?(Y or N) ')
        elif choice == 5:
            artworkSearch = input('What artwork would you like to delete? ')
            artworkDeleted = Artwork.delete().where(Artwork.artwork == artworkSearch)
            print('Artwork Deleted: ', artworkDeleted)
            catalogContinue = input('Would you like to continue?(Y or N) ')
        elif choice == 6:
            artworkSearch = input('What artwork would you like to change the availability on? ')
            newAvailability = input('Is this artwork Available or Sold? ')
            availabilityChanged = Artwork.update(availability = newAvailability).where(Artwork.artwork == artworkSearch).execute()
            print('The following availability has been changed', availabilityChanged)
            catalogContinue = input('Would you like to continue?(Y or N) ')
    else:
        print('Goodbye!!')

if __name__ == '__main__':
    main()
