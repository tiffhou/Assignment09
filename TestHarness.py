#------------------------------------------#
# Title: Test Harness
# Desc: A Module to test the Modules
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# THou, 2020-Mar-19, added formatting, added 3rd track to test with
# THou, 2020-Mar-22, added testing for generate_cd_id, remove_track()


import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IO

lstOfCDObjects = []
file_name = ['TestCD.txt', 'TestTrack.txt']


#------------------- Track Class ------------------ #
print('\n\n[[ Testing Track class ]]')
print(DC.Track.__doc__)
trk1 = DC.Track(1, 'test.track1', '01:59')
trk2 = DC.Track(2, 'test.track2', '02:59')
trk3 = DC.Track(3, 'test.track3', '03:59')
print(trk1)
print('record for file:', trk1.get_record())



#------------------ CD Class ------------------#
print('\n\n\n\n[[  Testing CD class ]]')
print(DC.CD.__doc__)

print('\nTEST: CD functionality (generate_cd_id())')
cd1_id = PC.DataProcessor.generate_cd_id(lstOfCDObjects)
cd1 = DC.CD(cd1_id, 'test_title', 'cd_artist')
print(cd1)
print('record for file (cd.get_record):',cd1.get_record())

print('TEST: adding tracks to CD 1 (cd.add_track())')
cd1.add_track(trk1)
cd1.add_track(trk2)
cd1.add_track(trk3)
print('get tracks (cd.get_tracks()):\n',cd1.get_tracks())
print('\nget long record (title & tracks):\n', cd1.get_long_record())

print('TEST: removing track 2...(remove_track())')
cd1.rmv_track(2)
print('get long record (title & tracks):\n', cd1.get_long_record())
lstOfCDObjects.append(cd1)





#------------------ Testing File IO ------------------#
print('\n\n\n\n[[ Testing of class FileIO ]]')

print('Saving file. (save_inventory())')
IO.FileIO.save_inventory(file_name, lstOfCDObjects)
print('file saved.\n')

print('Clearing inventory list')
lstOfCDObjects = []
print('# of items in table: ',len(lstOfCDObjects))

print('\nLoading file. (load_inventory())')
lstOfCDObjects = IO.FileIO.load_inventory(file_name)
print('file loaded.')
print('# of items in table: ',len(lstOfCDObjects))




#------------------ Testing Screen IO ------------------#
print('\n\n\n\n[[ Testing ScreenIO class ]]')

print('TEST: Main menu (print_menu()):')
IO.ScreenIO.print_menu()
print('selection in menu (menu_choice()): {}\n'.format(IO.ScreenIO.menu_choice()))

print('\nTEST: adding second CD object & displaying Inventory')
IO.ScreenIO.show_inventory(lstOfCDObjects)
print('\nadding second CD...')
cd2_id = PC.DataProcessor.generate_cd_id(lstOfCDObjects)
cd2 = DC.CD(cd2_id, 'test_title_2', 'cd_artist_2')
lstOfCDObjects.append(cd2)
print('\nInventory (printing cd as string):')
for item in lstOfCDObjects:
    print(item)

print('\nTEST: CD 1 Tracks')
cd_idx = 1
cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)

print('Test: show Tracks for CD 1: (show_tracks())')
IO.ScreenIO.show_tracks(cd)

print('\nSub Menu (print_CD_menu())')
IO.ScreenIO.print_CD_menu()
print('selection in sub menu (menu_CD_choice()): {}'.format(IO.ScreenIO.menu_CD_choice()))



#------------------ Testing Processing Classes ------------------#
print('\n\n\n\n[[ Testing Processing Classes ]]')

print('\nAdding CD (add_cd()):')
test_id = PC.DataProcessor.generate_cd_id(lstOfCDObjects)
PC.DataProcessor.add_CD(test_id, ('Foreigner', 'Foreigner'), lstOfCDObjects)
print('CD Inventory:')
for item in lstOfCDObjects:
    print(item)



