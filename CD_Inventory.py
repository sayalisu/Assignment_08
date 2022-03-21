#------------------------------------------#
# Title: CD_inventory.py
# Desc: CD_inventory - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Sayali, 2022-March-20, completed the TODOs
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # DONE Add Code to the CD class
    def __init__(self,CD_ID,CD_TITLE,CD_ARTIST):
        self.__cd_id = CD_ID
        self.__cd_title = CD_TITLE
        self.__cd_artist = CD_ARTIST
               
    @property
    def cd_id(self):
        return int(self.__cd_id)
    @cd_id.setter
    def cd_id(self,ID):
        if type(ID) == 'int':
            self.__cd_id = ID
        else:
           raise Exception ('Not an integer')
       
    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self,Title):
        self.__cd_title = Title 
        
    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self,Artist):
            self.__cd_artist = Artist
      
    #methods
    def add_list_of_obj(cdObj):
          lstOfCDObjects.append(cdObj)
          return lstOfCDObjects
    def __str__(self):
        str_new = ''
        str_new = str_new +  str(self.__cd_id) + ', ' + self.__cd_title + ', ' + self.__cd_artist +'\n'
        return str_new
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # DONE Add code to process data from a file
    # DONE Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
         
            file1 =open(file_name,'w') 
            for row in lst_Inventory:
                 str1 = str(row.cd_id) + ', ' + row.cd_title + ', ' + row.cd_artist + '\n'
                 file1.write(str1)
            file1.close() 

    
    @staticmethod
    def load_inventory(file_name):
        lstOfCDObjects.clear()
        try :
            file1 =open(file_name,'r')
            for row in file1:
                data = row.strip().split(',')
                CdInfo = CD(int(data[0]),data[1],data[2])
                lstOfCDObjects.append(CdInfo)
            file1.close()
        except FileNotFoundError:
            print("Filenot_found,please make sure file is present")
        except EOFError:
                print("File has no contents.Please add data to the file and then read")
        except ValueError:
                        print("Check the values")
        return lstOfCDObjects


# -- PRESENTATION (Input/Output) -- #
class IO:
    # Done add docstring
    # DONE add code to show menu to user
    # DONE add code to captures user's choice
    # DONE add code to display the current data on screen
    # DONE add code to get CD data from user
   """Handling Input / Output
   
   properties:
       
   methods:
       print_menu(): -> None
       menu_choice(): -> (choice user has selcted from the menu)
       show_inventory(): -> (Shows the current inventory )
       add_inventory(): -> (CDObject -> Object of class CD with all attributes.)
   
   """
   @staticmethod
   def print_menu():
       """Displays a menu of choices to the user

       Args:
           None.

       Returns:
           None.
       """

       print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
       print('[s] Save Inventory to file\n[x] exit\n')

   @staticmethod
   def menu_choice():
       """Gets user input for menu selection

       Args:
           None.

       Returns:
           choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

       """
       choice = ' '
       while choice not in ['l', 'a', 'i',  's', 'x']:
           choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
       print()  # Add extra space for layout
       return choice

   @staticmethod
   def show_inventory(table):
       """Displays current inventory table


       Args:
           table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

       Returns:
           None.

       """
       print('======= The Current Inventory: =======')
       print('ID\tCD Title Artist\n')
       for row in table:
             print(row.__str__())
       print('======================================')
   @staticmethod
   def add_inventory():
       '''
       This is used to take the inputs from the user and store to variables which it returns 
       as strID, strTitle, str Artist
       
       Arguemnts/Parameters:
           None
       
       Returns:CDObject -> Object of class CD with all attributes.

       '''
       intID = None
       strTitle = ''
       stArtist = ''
       while type(intID) != int:
           try:
               intID = int(input('Enter ID: ').strip())
           except ValueError :
               print("This ID is not integer type , please enter integer ")
           
       strTitle = input('What is the CD\'s title? ').strip()
       stArtist = input('What is the Artist\'s name? ').strip()
       CdObject = CD (intID, strTitle, stArtist) 
       return  CdObject
    
   
  
# -- Main Body of Script -- #
# DONE Add Code to the main body

lstOfCDObjects =FileIO.load_inventory(strFileName)

while True:
    
     # 2.1 Display Menu to user and get choice
     IO.print_menu()
     strChoice = IO.menu_choice()
    
     # 3. Process menu selection
     # 3.1 process exit first
     if strChoice == 'x':
         break
     # 3.2 process load inventory
     if strChoice == 'l':
         print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
         strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
         if strYesNo.lower() == 'yes':
             print('reloading...')
             FileIO.load_inventory(strFileName)
             IO.show_inventory(lstOfCDObjects)
         else:
             input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
             IO.show_inventory(lstOfCDObjects)
         continue  # start loop back at top.
     # 3.3 process add a CD
     elif strChoice == 'a':
         CDObject = IO.add_inventory()
         lstOfCDObjects =CD.add_list_of_obj(CDObject)
         IO.show_inventory(lstOfCDObjects)
         continue  # start loop back at top.
     # 3.4 process display current inventory
     elif strChoice == 'i':
         IO.show_inventory(lstOfCDObjects)
         continue  # start loop back at top.
     # 3.6 process save inventory to file
     elif strChoice == 's':
         # 3.6.1 Display current inventory and ask user for confirmation to save
         IO.show_inventory(lstOfCDObjects)
         strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
         # 3.6.2 Process choice
         if strYesNo == 'y':
             FileIO.save_inventory(strFileName, lstOfCDObjects )
             # 3.6.2.1 save data
             # DONE move processing code into function
         else:
             input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
         continue  # start loop back at top.
     # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
     else:
         print('General Error')

