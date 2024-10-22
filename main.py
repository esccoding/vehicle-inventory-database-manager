#### main.py ####
from modules.vehicle_inventory import *

inventory = VehicleInventory()

print('\n--- Welcome to the Vehicle Inventory database! ---')

user_menu_input = ''
while user_menu_input != 'quit':
    print('_' * 50)
    print('\nWhat would you like to do?')
    user_menu_input = input("> 'New' to add vehicle entry\n> 'Mod' to update existing entry\n> 'Del' to remove existing entry\n> 'Find' to search for existing entry\n> 'View' to view full vehicle inventory\n> 'Save' to save vehicle database to file\n> 'Quit' to exit program\n").replace(' ','').lower()


    # user enter new vehicle entry    
    if user_menu_input == 'new':
        print('_' * 50)
        print('\n### New Entry ###\n')
        stock_num = input('Enter vehicle stock number:\n').replace(' ','').upper()
        make = input('Enter make:\n').replace(' ','').capitalize()
        model = input('Enter model:\n').replace(' ','').capitalize()
        color = input('Enter color:\n').replace(' ','').capitalize()
        year = input('Enter year:\n').replace(' ','')
        mileage = input('Enter mileage:\n').replace(' ','')
        inventory.add_vehicle(stock_num, make, model, color, year, mileage)
        print(inventory.display_vehicle(stock_num))
    
    # user modify existing entry
    elif user_menu_input == 'mod':
        print('_' * 50)
        print('\n### Update Entry ###\n')
        stock_num = input('Enter vehicle stock number:\n').replace(' ','').upper()
        if stock_num in inventory.inventory:  
            print(inventory.display_vehicle(stock_num))
            make = input('\nEnter make:\n').replace(' ','').capitalize()
            model = input('Enter model:\n').replace(' ','').capitalize()
            color = input('Enter color:\n').replace(' ','').capitalize()
            year = input('Enter year:\n').replace(' ','')
            mileage = input('Enter mileage:\n').replace(' ','')
            inventory.update_vehicle(stock_num, make, model, color, year, mileage)
            print(inventory.display_vehicle(stock_num))
        else:
            print('\nVehicle not found in inventory.')

    # user delete existing entry
    elif user_menu_input == 'del':
        print('_' * 50)
        print('\n### Delete Entry ###\n')
        stock_num = input('Enter vehicle stock number:\n').replace(' ','').upper()
        if stock_num in inventory.inventory:
            print(inventory.display_vehicle(stock_num))
            confirm_delete_open = True
            while confirm_delete_open:
                confirm_delete = input(f"\nAre you sure you want to delete the entry for {stock_num}?\nEnter 'yes' or 'no':\n").replace(' ','').lower()
                if confirm_delete == 'yes':
                    inventory.remove_vehicle(stock_num)
                    print(f'\nEntry for {stock_num} successfully deleted.')
                    confirm_delete_open = False
                elif confirm_delete == 'no':
                    confirm_delete_open = False
                    pass
                else:
                    print('\nError: entry not recognized.')
                    pass
        else:
            print('\nVehicle not found in inventory.')

    # user search vehicle inventory
    elif user_menu_input == 'find':
        print('_' * 50)
        print('\n### Search Inventory ###\n')
        stock_num = str(input('Enter vehicle stock number:\n')).replace(' ','').upper()
        print(inventory.display_vehicle(stock_num))

    # user view inventory - keys only or full
    elif user_menu_input == 'view':
        print('_' * 50)
        print('\n### View Inventory ###\n')
        inventory.view_inventory()

    # user save inventory data to text file
    elif user_menu_input == 'save':
        file = open('inventory.txt', 'w')
        for key, value in inventory.inventory.items():    
            file.write('Stock# {} :\n {}\n\n'.format(key, value))
        print("\n. . . . . Inventory data saved successfully to 'inventory.txt'")
        file.close()

    
    elif user_menu_input not in ['find','new','mod','del','view','save', 'quit']:
        print('\nError: entry not recognized.')
        pass

# close program
else:
    print('\nThank you for using the Vehicle Inventory database!\nExiting...')
    exit()