#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# THou, 2020-Mar-20, added generate_cd_id()
# Thou, 2020-Mar-21, added code for tracks
# Thou, 2020-Mar-22, added error handling, updated docstrings
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application
    
    methods:
        generate_cd_id(table) -> cd_id: generates a unique CD ID
        add_CD(cdId, CDInfo, table) -> None: adds a CD instance
        select_cd(table, cd_idx) -> CD: selects and returns a CD instance
        add_track(track_info: tuple, cd: DC.CD) -> None: creates a track and appends to a CD
        remove_track(track_pos: int, cd: DC.CD) -> None: removes a track from a CD
    """

    @staticmethod
    def generate_cd_id(table: list) -> str:
        """generates a CD ID, checks for uniqueness in current inventory
        
        Args:
            table (list): the current inventory table
        
        Return:
            cd_id (int): the auto-generated CD ID
        """
        cd_id = 1
        if table is not None:
            for cd in table:
                if cd.cd_id == cd_id:
                    cd_id += 1
        return cd_id

    @staticmethod
    def add_CD(cdId, CDInfo, table) -> None:
        """function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Raises:
            ValueError Exception: if ID is not integer

        Returns:
            None.
        """
        title, artist = CDInfo
        try:
            cdId = int(cdId)
        except ValueError as e:
            raise Exception('ID must be an Integer!\n' + str(e))
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            ValueError Exception: if ID is not an integer
            Exception: If id is not in list.

        Returns:
            cd (DC.CD): CD object that matches cd_idx
        """
        try:
            cd_idx = int(cd_idx)
            try:
                for row in table:
                    if row.cd_id == cd_idx:
                        cd = row
                return cd
            except Exception as e:
                print('ID is not in inventory.\n' + str(e))
        except ValueError as e:
            print('ID must be an integer.')
            print(e.__doc__)

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd
        
        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the track gets added to.
            
        Raises:
            ValueError exception: raised in case position is not an integer.
            
        Returns:
            None.
        """
        position, title, length = track_info
        try:
            position = int(position)
            track = DC.Track(position, title, length)
            cd.add_track(track)
        except ValueError:
            print('Position must be an integer.\n')

    @staticmethod
    def remove_track(track_pos: int, cd: DC.CD) -> None:
        """removes a track from the CD
        
        Args:
            track_pos (int): the position of the track to be removed
            cd (DC.CD): the cd object the track is to be removed from
        
        Raises:
            ValueError Exception: raised in case position is not an integer.
            Exception: raised in case the track does not exist
        
        Returns:
            None
        """
        try:
            track_pos = int(track_pos)
            try:
                cd.rmv_track(track_pos)
            except Exception as e:
                print('Track does not exist.\n', str(e))
        except ValueError:
            print('Position must be an integer.')
