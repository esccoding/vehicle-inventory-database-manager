class VehicleInventory: # create vehicle inventory class
    def __init__(self):
        self.inventory = {} # create a dictionary to store inventory data

    # allow user to add a new vehicle to inventory    
    def add_vehicle(self, __stock_num, __make, __model, __color, __year, __mileage):
        try:
            self.inventory[__stock_num] = {
                'make': str(__make),
                'model': str(__model),
                'color': str(__color),
                'year': int(__year),
                'mileage': int(__mileage)
            }
            print(f'\nEntry for {__stock_num} successfully added:')
        except ValueError:
            print('\n>>> Error: both Year and Mileages must be integers.')
            pass
            
    # allow modification of existing entries
    def update_vehicle(self, __stock_num, __make, __model, __color, __year, __mileage):
        try:
            if __stock_num in self.inventory:
                self.inventory[__stock_num]['make'] = str(__make)
                self.inventory[__stock_num]['model'] = str(__model)
                self.inventory[__stock_num]['color'] = str(__color)
                self.inventory[__stock_num]['year'] = int(__year)
            else:
                print('\nVehicle not found in inventory.')
        except ValueError:
            print('\n>>> Error: Year must be an integer - modification not made.')
        try:
            self.inventory[__stock_num]['mileage'] = int(__mileage)
        except ValueError:
            print('\n>>> Error: Mileage must be an integer - modification not made.')
        finally:
            print('\n### Result ###')

    # allow user to remove a vehicle from inventory
    def remove_vehicle(self, __stock_num):
        if __stock_num in self.inventory:
            del self.inventory[__stock_num]
        else:
            print('\nVehicle not found in inventory.')

    # displays vehicle information stored in inventory dictionary
    def display_vehicle(self, __stock_num):
        if __stock_num in self.inventory:
            return f"\nStock Number: {__stock_num}\nMake: {self.inventory[__stock_num]['make']}\nModel: {self.inventory[__stock_num]['model']}\nColor: {self.inventory[__stock_num]['color']}\nYear: {self.inventory[__stock_num]['year']}\nMileage: {self.inventory[__stock_num]['mileage']}"
        else:
            return '\nVehicle not found in inventory.'

    # display entire vehicle inventory
    def view_inventory(self):
        view_menu_open = True
        while view_menu_open:
            self.view_option = input("Select preferred inventory view:\n> 'ID' to view stock numbers only\n> 'Full' to view all entry information:\n").replace(' ','').lower()
            if self.view_option == 'id':
                print('\n### Inventory by Stock Numbers ###\n')
                print(self.inventory.keys())
                view_menu_open = False
            elif self.view_option == 'full':
                print('\n### Full Inventory ###\n')
                for key, value in self.inventory.items():
                    print('{} : {}'.format(key, value))
                view_menu_open = False
            else:
                print('\nError: entry not recognized.\n')
                pass
        