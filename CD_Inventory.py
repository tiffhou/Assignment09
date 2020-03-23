    #------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# THou, 2020-Mar-20, added generate_cd_id() function
# THou, 2020-Mar-21, added submenu code
# THou, 2020-Mar-22, added error handling for selecting a nonexistent CD, tweaked formatting
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        print('Thanks for using the CD Inventory. Goodbye!')
        break

    #load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    #add a CD
    elif strChoice == 'a': 
        cd_idx = PC.DataProcessor.generate_cd_id(lstOfCDObjects)
        print('CD ID: ', cd_idx)
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(cd_idx, tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    #display inventory table
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    #select CD
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while cd is not None:
            IO.ScreenIO.show_tracks(cd)
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()

            #exit to main menu
            if strChoice == 'x':
                break
            # add track to CD
            if strChoice == 'a':
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo, cd)
                continue
            #display CD details
            elif strChoice == 'd':
                print(cd.get_long_record())
                pass
            #remove track from CD
            elif strChoice == 'r':
                track_idx = input('Which track would you like to delete? ')
                PC.DataProcessor.remove_track(track_idx, cd)
                pass
            else:
                print('Invalid selection.')
        continue


    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.


    else:
        print('General Error')
        continue