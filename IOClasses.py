#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# THou, 2020-Mar-20, added formatting when displaying data
# THou, 2029-Mar-21, added select CD option, added code for submenu handling
# THou, 2020-Mar-22, tweaked error handling, updated docstrings
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:
        
    properties:
        None
        
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """saves CD and track objects to files

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.
        """
        file_name_CD, file_name_Track = file_name
        try:
            #save CD objects
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            #save track objects
            with open(file_name_Track, 'w') as file:
                for disc in lst_Inventory:
                    for track in disc.cd_tracks:
                        if track is not None:
                            data = '{},{}'.format(disc.cd_id, track.get_record())
                            file.write(data)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """loads cds and tracks from file into memory

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.
        """
        file_name_CD, file_name_Track = file_name
        lst_Inventory = []
        try:
            #load cd file
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            #load track file
            with open(file_name_Track, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    new_track = DC.Track(int(data[1]), data[2], data[3])
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(data[0]))
                    cd.add_track(new_track)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory



class ScreenIO:
    """Handling Input / Output
    
    methods:
        print_menu(): shows main menu
        menu_choice(): gets input for main menu
        print_CD_menu(): shows submenu for a CD
        menu_CD_choice():
    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('\n\n[[  Main Menu  ]]\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice() -> str:
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu() -> None:
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """
        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice() -> str:
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x
        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table) -> None:
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd) -> None:
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.
        """
        print('\n====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        try:
            print(cd.get_tracks())
        except AttributeError:
            print('No tracks to display')
        print('=================================\n')

    @staticmethod
    def get_CD_info() -> str:
        """function to request CD information from User to add CD to inventory
        
        Args:
            None
        
        Returns:
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.
        """
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdTitle, cdArtist

    @staticmethod
    def get_track_info() -> str:
        """function to request Track information from User to add Track to CD / Album
        
        Args:
            None
        
        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.
        """
        trkId = input('Enter Position on CD / Album: ').strip()
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength
