# Data Reference: #https://www.kaggle.com/mrpantherson/board-game-data

# Import JSON module
import json

#Initialize Set pf Data in an Array
boardgames = [{"name": "Gloomhaven", "rank": "1", "cost": "140", "year": "2017"}, 
              {"name": "Pandemic Legacy: Season 1", "rank": "2", "cost": "90", "year": "2015"}, 
              {"name": "Through the Ages: A New Story of Civilization", "rank": "3", "cost": "60", "year": "2015"},
              {"name": "Terraforming Mars", "rank": "4", "cost": "70", "year": "2016"},
              {"name": "Twilight Struggle", "rank": "5", "cost": "65", "year": "2005"},
              {"name": "Star Wars: Rebellion", "rank": "6", "cost": "115", "year": "2016"},
              {"name": "Scythe", "rank": "7", "cost": "80", "year": "2016"},
              {"name": "Terra Mystica", "rank": "8", "cost": "83", "year": "2012"},
              {"name": "Great Western Trail", "rank": "9", "cost": "95", "year": "2016"},
              {"name": "The 7th Continent", "rank": "10", "cost": "99", "year": "2017"},
              {"name": "Gaia Project", "rank": "11", "cost": "130", "year": "2017"},
              {"name": "The Castles of Burgundy", "rank": "12", "cost": "65", "year": "2011"},
              {"name": "7 Wonders Duel", "rank": "13", "cost": "40", "year": "2015"},
              {"name": "War of the Ring", "rank": "14", "cost": "100", "year": "2012"},
              {"name": "Caverna: The Cave Farmers", "rank": "15", "cost": "97", "year": "2013"},
              {"name": "Puerto Rico", "rank": "16", "cost": "43", "year": "2002"},
              {"name": "Agricola", "rank": "17", "cost": "50", "year": "2007"},
              {"name": "Mage Knight Board Game", "rank": "18", "cost": "90", "year": "2011"},
              {"name": "Viticulture Essential Edition", "rank": "19", "cost": "62", "year": "2015"},
              {"name": "Arkham Horror: The Card Game", "rank": "20", "cost": "60", "year": "2016"},
              {"name": "Mansions of Madness: Second Edition", "rank": "21", "cost": "150", "year": "2016"},
              {"name": "Concordia", "rank": "22", "cost": "47", "year": "2013"},
              {"name": "Blood Rage", "rank": "23", "cost": "180", "year": "2015"},
              {"name": "Mechs vs. Minions", "rank": "24", "cost": "175", "year": "2016"},
              {"name": "Star Wars: Imperial Assault", "rank": "161", "cost": "140", "year": "2014"},
              {"name": "Orléans", "rank": "26", "cost": "48", "year": "2014"}, 
              {"name": "Through the Ages: A Story of Civilization", "rank": "27", "cost": "63", "year": "2006"},
              {"name": "Food Chain Magnate", "rank": "28", "cost": "140", "year": "2015"},
              {"name": "Power Grid", "rank": "29", "cost": "40", "year": "2004"},
              {"name": "A Feast for Odin", "rank": "30", "cost": "99", "year": "2016"}]

faves = []
users = []

def newUser(username, password):
    return{
        "username": username,
        "password": password,
        "faves": []
    }

json_string = json.dumps(boardgames) 

class BG:
    def __init__(self, nameinit, rankinit, costinit, yearinit): 
        #Properties
        self.name = nameinit
        self.rank = rankinit
        self.cost = costinit
        self.year = yearinit
        
def displayGame():
    for game in boardgames:
        print(game["name"])
             
def searchGame():
    minCost = input("Choose the minimum cost of a boardgame you would like to buy: ")
    maxCost = input("Choose the maximum mum cost of a boardgame you would like to buy: ")
    for game in boardgames:
        if int(game["cost"]) >= int(minCost) and int(game["cost"]) <= int(maxCost):
            print(game["name"])
            
def addfavourites():
    displayGame()
    favgame = input("Choose a boardgame to add to favourites list: ")
    for game in boardgames:
        if game["name"] == favgame:
            faves.append(favgame)
            
def removefavourites():
    displayfavourites()
    favgame = input("Choose a boardgame to remove from favourites list: ")
    for game in faves:
        if game["name"] == favgame:
            faves.remove(favgame)           
    
def displayfavourites():
    for game in faves:
        print(game)
                         

def menuOptions():
    selection = 0 
    while selection != 6:
        print(f'''
        Main Menu
        
            1. Display All Boardgames
            2. Search Boardgame by Cost
            3. Add Boardgame to Favourites List
            4. Remove Boardgame From Favourites List
            5. Display Favourites List
            6. Exit
            ''')
        selection = input("Type a number corresponding with it's option please: ")
        if selection == "1":
            displayGame()
        elif selection == "2":
            searchGame()
        elif selection == "3":
            addfavourites()
        elif selection == "4":
            removefavourites()
        elif selection == "5":
            displayfavourites()
        elif selection == "6":
            print("Program Closed.")
            quit()
menuOptions()        
            
#def login():        
    #username = input("Please print your username: ")
    #password = input("Please print your password: ")  
    #for names in users:  
        #if username == -1:
            #print("Username not found.")
        #elif password == -1:
            #print("Incorrect Password.")
        #elif username == names["username"] and password == names["password"]:
            #print("Welcome back " + names["username"])
                    
#def mainMenu():       
    #selection = 0
    #while selection != 4:
        #print(f'''
            #Main Menu
        
           #1. Login
           #2. Sign Up
            #3. Exit
            #''')  
    #selection = input("Type a number corresponding with it's option please: ")
    #if selection == "1":
        #login()
        
        
        
        
        

        
    
        
    
            
