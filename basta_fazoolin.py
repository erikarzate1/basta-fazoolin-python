class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    """
    Initialize a Menu object.
    
    Parameters:
    -----------
    name : str
        The name of the restaurant
    items : str
        Menu items for particular time frame
    start_time : str
        Start time(in military form) when menu will be served 
         Time in 24-hour format (e.g., 1430 for 2:30 PM)
    end_time : str
      End time (in military form )when menu stop being served
       Time in 24-hour format (e.g., 1430 for 2:30 PM)

    """
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  #Class representation 
  def __repr__(self):
    """
    Return a string representation of the Menu object.
      
    Returns a string that includes the Menu name and what times (in military form) it is served 
   

    """
    return f"{self.name} menu is available from  {self.start_time} to {self.end_time} "
  
  # Calculates bill
  def calculate_bill(self, purchased_items):
    """
    Return bill  given purchased menu items 
    
    Parameters:
    -----------
    purchased items : list 
        
        
    Returns:
    --------
    str
        Formatted string of available menus
    """
    bill  = 0
    for purchased_item in purchased_items:
      if purchased_item  in self.items:
        bill = bill + self.items[purchased_item]
    return bill 

  def Meal (self):
    return ("The name of the menu is " + self.name)
  
#Breakfast/Brunch Items 
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50 }
#Early Bird  Items 
early_bird_menu = {
   'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00, }
#Dinner food items
dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
# Kids food items 
kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00 }

brunch = Menu("brunch", brunch_items, "1100", "1600")
early_bird = Menu("early_bird", early_bird_menu, "1500", "1800")

# print(brunch.Meal())
# Indicate when specific menu is available 
print(brunch.__repr__())
#Calculate bill for specific brunch items
print(brunch.calculate_bill(['pancakes', 'waffles', 'home fries']))
#Calculate bill for specific early bird items
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

################################################

class Franchise:
  def __init__(self, address, menus):
    """
    Initialize a Franchise object.
    
    Parameters:
    -----------
    address : str
        The address of the restaraunt location
    menus : list
        Menu available for this restaraunt given list: brunch, early_birds, dinner, kids 
    """
    self.address = address
    self.menus = menus 
  
  def __repr__(self):
     """
      Returns a string representation of the Franchise object.
      
      Returns a string that includes the restaraunt adress and the types of food menus available . For example, dinner, and brunch. 

     """

     menu_string = (", ").join(self.menus)
     return f"Restaraunt address is {self.address}. Its menus include the following: " + str(menu_string) 
  
  def available_menus(self, time):
    """
    Return food menu available given a specific time (military form)
    
    Parameters:
    -----------
    time : string

    Time person intends to eat at restaraunt
        
        
    Returns:
    --------
    str
        Formatted string food menu available given a specific time (military form)
    """ 

    ##Convert string time into an type int
    self.time = int(time)  
    menu_list = [ ]
    #Checks if restaraunt is open. Else, inform customer restarauant is closed
    if  1100 <= self.time <= 2300:
      #Check time frames and determine best restaraunts fit time frame 
      if  1100 <= self.time  <= 1500: 
        menu_list.append('brunch') 
      if  1100 <= self.time  <= 2100: 
        menu_list.append('Kids_menu') 
      if  1500 <= self.time  <= 1800: 
        menu_list.append('early_bird') 
      if  1700 <= self.time  <= 2300: 
        menu_list.append('dinner') 
    else :
      menu_list.append("We are Closed. Come at a later time")
   
    #Conver menu_list array/string to a new object menu_string that can be printed without brackets
    menu_string = (", ").join(menu_list)
    return f"For time {self.time},  menus available include: " + str(menu_string)

#Create Franchise "Flagschip " with specific address and menu offerings
Flagship = Franchise("1232 West End Road",["brunch_items", "early_bird_menu", "dinner_menu", "kids_menu"] )

#Create Franchise "new_installment " with specific address and menu offerings
new_installment = Franchise("12 East Mulberry Street",["brunch_items", "early_bird_menu", "dinner_menu", "kids_menu"] )

# print(Flagship("1232 West End Road"))
print(Flagship.__repr__())
print(Flagship.available_menus("1500"))



##########################################

class Business:
  def __init__ (self, name, franchises):
    """
    Initialize a Business object.
    
    Parameters
    -----------
    name : 
        The name of the business 
    franchises : 
        The name of franchises  
    """
    self.name = name
    self.franchises = franchises


arepa_biz = Business("Basta Fazoolin' with my Hearts", ['flagship_store', 'new_installment'])



arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)



