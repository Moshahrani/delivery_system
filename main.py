# Moshfeq Shahrani
# ID - 011919956
# C950 
# Task 2


import csv
from datetime import datetime, timedelta

from hashTable import CustomHashTable
from package import Package
from truck import Truck

#   linear time complexity O(n) due to reading the data, 
#   creating the new package object and assigning the values for each package attribute
#   hash table is also O(n) space complexity as it stores all csv data one time by package   

def loadPackagesFromCSV(filename, hash_table):

    with open(filename) as packages:
        packageData = csv.reader(packages, delimiter=',')
        
        #  extracting all attributes and creating a new package Object for each package's data

        for package in packageData:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            delivery_time = package[5]
            weight = package[6]
            status = 'WGUPS Hub'
        
            newPackage = Package(
                ID=package_id, address=address, city=city, state=state,
                zip_code=zip_code, delivery_time=delivery_time, weight=weight,
                status=status
            )
            
            # putting package object into hash table
            #  if already exists, print error

            if not hash_table.add(package_id, newPackage):
                        print(f"Error: Package with ID {package_id} already exists in the hash table.")
            # else:
            #     print(f"Package ID {package_id} added successfully.")



packages_hash = CustomHashTable()
loadPackagesFromCSV('./packageCSV.csv', packages_hash)


#   O(n) time and space complexity
#   method to load distances from csv to a list for a 2 x 2 matrix 

def loadDistanceData(filename):
     
     with open(filename) as distances:
          data = csv.reader(distances, delimiter=',')
          for row in data:
                distance_data.append(row)
               

distance_data = []
loadDistanceData('./distanceCSV.csv')

#   O(n) time and space complexity
#   Reading all data once and extracting addresses to list

def loadAddressData(filename):
     
     with open(filename) as addresses:
          data = csv.reader(addresses, delimiter=',')
          for row in data:
               address_data.append(row)


address_data = []
loadAddressData('./addressCSV.csv')

#   O(1) constant time operation
#   calculating distance between two addresses

def distance_between(address1, address2, address_index_map, distance_data):
    index1 = address_index_map[address1]
    index2 = address_index_map[address2]
    distance = distance_data[index1][index2]

    # check for reverse in case of blank data (" ") 

    if distance == '':
        distance = distance_data[index2][index1]
    return float(distance)

#   O(n) time complexity for searching through list of packages one time
#   finds the package in truck with nearest dropoff address to current truck location

def closest_from_truck(truck):
    minimum_distance = float('inf')
    closest_package = None
    closest_package_address = None
    
    #   finds closest address of all remaining packages

    for package_id in truck.packages:
        package = packages_hash.search(int(package_id)) 
        if package is not None:
            distance = distance_between(truck.location, package.address)
            if distance < minimum_distance:
                minimum_distance = distance
                closest_package_id = package_id
                closest_package_address = package.address
    
    if closest_package:
         return closest_package_id, closest_package_address
    else:
         return None


# Truck instances and manually loading the packages (ID) with a departure time

truck1 = Truck(16, 0, 18, [13,14,15,16,19,20,27,29,30,31,34,37,40], '4001 South 700 East', timedelta(hours=0), 1)
truck2 = Truck(16, 0, 18, [1,3,4,5,6,9,18,26,28,32,35,36,38], '4001 South 700 East', timedelta(hours=1, minutes=5), 2)
truck3 = Truck(16, 0, 18, [2,7,8,10,11,12,17,21,22,23,24,25,33,39], '4001 South 700 East', timedelta(hours=2, minutes=30), 3)

truck_list = [truck1, truck2, truck3]

#  O(n) time complexity operation for labeling proper truck id for each package
for truck in truck_list:
    for package_id in truck.packages:
        package = packages_hash.search(package_id)
        if package:
            package.truck_id = truck.ID

#  keeping track of departure times for cli data retrieval

truck_departure_times = {
    1: truck1.departure_time,
    2: truck2.departure_time,
    3: truck3.departure_time
}


# O(n) space complexity
# O(n) time complexity
# smooth mapping of address in address index map object for address referencing during deliveries

def loadAddressIndexMap(filename):
    address_index_map = {}
    with open(filename) as file:
        reader = csv.reader(file)

        # getting the address from the right position in file
        for index, row in enumerate(reader):
            address = row[2].strip() 
            address_index_map[address] = index
    return address_index_map

address_index_map = loadAddressIndexMap('./addressCSV.csv')

# --------------------------------------------------------------

# O(1) constant time operations for all operations in this updating variables algorithm

def update_truck_and_package(truck, package, distance):

    # update truck's location to package address
    truck.location = package.address

    # Calculation of time taken traveling 
    # updating truck's departure time also

    travel_time = timedelta(minutes=(distance / truck.speed) * 60)
    truck.departure_time += travel_time

    # updating total miles of truck

    truck.mileage += distance
    truck.mileage = round(truck.mileage, 2)

    # marking the package's delivery status as "delivered" 
    # recording the delivery time as a datetime object

    package.status = 'delivered'
    package.delivery_time = truck.departure_time.strftime('%H:%M:%S')

    # logging the package's delivery time with address and total miles of truck plus current truck location
    print(f"Package {package.ID} delivered to {package.address} at {package.delivery_time}.")


# O(n^2) time complexity
# algorithm for delivering packages 

def truck_deliver_packages(truck, packages_hash, address_index_map, distance_data):
    undelivered_packages = []

    # queueing up list with packages for truck before takeoff
    for package_id in truck.packages:
        package = packages_hash.search(package_id)
        if package:
            undelivered_packages.append(package)
            print(f"Added Package ID {package_id} to undelivered_packages.")
    

    # O(n) time complexity
    # start of search for nearest package 

    while undelivered_packages:
        nearest_package = None
        shortest_distance = float('inf')

        # O(n) time complexity
        # calculations for finding nearest package

        for package in undelivered_packages:
            distance = distance_between(truck.location, package.address, address_index_map, distance_data)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_package = package

           # Check if the nearest package is package #9 and correct the address if necessary

        if nearest_package and nearest_package.ID == 9:
            nearest_package.address = "410 S State St"
            nearest_package.city = "Salt Lake City"
            nearest_package.state = "UT"
            nearest_package.zip_code = "84111"
            print("Fixed address for package #9")

        #  if not package #9 , proceed to update truck miles, delivery stats, and offload package

        if nearest_package:
            update_truck_and_package(truck, nearest_package, shortest_distance)
            undelivered_packages.remove(nearest_package)
            # print(f"Delivered package {nearest_package.ID} to {nearest_package.address}. Remaining packages: {len(undelivered_packages)}")

    print(f"All packages delivered. Total mileage for this trip: {truck.mileage} miles.")


# truck_deliver_packages(truck1, packages_hash)

truck_deliver_packages(truck1, packages_hash, address_index_map, distance_data)
truck_deliver_packages(truck2, packages_hash, address_index_map, distance_data)
truck_deliver_packages(truck3, packages_hash, address_index_map, distance_data)

#  printing a general report of all packages and delivery info, truck info

def general_report(ht, truck_list):
    print("Generating General Report...")
    delivered_packages = sum(1 for pkg_id in ht.get_all_keys() if ht.search(pkg_id).status == 'delivered')
    print("Number of packages delivered:", delivered_packages)
    print("Total mileage of all trucks:", sum(truck.mileage for truck in truck_list))


def query_specific_package(ht):
    package_id = input("Enter the package ID to query: ")
    package = ht.search(int(package_id)) 
    if package:
        print(f"Package ID: {package.ID}, Address: {package.address}, Status: {package.status}, Delivery Time: {package.delivery_time}")
    else:
        print("No package found with that ID.")

def package_status_at_time(ht, query_time):

    query_time = datetime.strptime(query_time, "%H:%M:%S").time()

    #   O(n) time complexity as all packages need to be found once for status retrieval

    found_packages = False
    for bucket in ht.table:
        for kvp in bucket:
            package = kvp[1]

            #  searching hash table for packages 
            
            try:
                delivery_time = datetime.strptime(package.delivery_time, "%H:%M:%S").time() if package.delivery_time else None
    
            except ValueError:
                print(f"Error converting delivery time for package ID {package.ID}")
                delivery_time = None

            #  convert time to datetime.time

            truck_departure_time = truck_departure_times.get(package.truck_id)
            truck_departure_time = truck_departure_time.time() if truck_departure_time else None

            #  get status of packages based on user input of time

            if truck_departure_time and query_time < truck_departure_time:
                package.status = "At Hub"
            elif delivery_time and query_time >= delivery_time:
                package.status = "Delivered"
            elif truck_departure_time and query_time >= truck_departure_time:
                package.status = "In transit"
            else:
                package.status = "At Hub"

            found_packages = True

            #  print all packages with their status at user inputted time 

            print(f"Package ID: {package.ID}, Status at {query_time.strftime('%H:%M:%S')}: {package.status}")

    if not found_packages:
        print("No packages found.")

#  interactive menu with a couple options including a general report, specific package info, query by time

def menu(ht, truck_list):
    while True:
        print("=====================")
        print("====== WGUPS ========")
        print("=====================")
        print("Please select a menu option for more information about a delivery.\n")
        print("\t 1. Full Report")
        print("\t 2. Package Info")
        print("\t 3. Query Packages by Delivery Time")
        print("\t 4. Exit")

        #  options for user to choose from
        #  can find info on packages and at certain times/status

        user_input = input("\nEnter your choice here: ")
        if user_input.isdigit():
            option = int(user_input)
            if option == 1:
                general_report(ht, truck_list)
            elif option == 2:
                query_specific_package(ht, truck_list)
            elif option == 3:
                while True:
                    query_time_str = input("Enter the query time (HH:MM:SS format) or type 'back' to return: ")
                    if query_time_str.lower() == 'back':
                        break
                    try:
                        package_status_at_time(ht, query_time_str)
                        break
                    except ValueError:
                        print("Error: Invalid time format. Please use HH:MM:SS format.")
            elif option == 4:
                print("The program will now close.")
                break
        else:
            print("Error: Not a valid option. Please enter 1, 2, 3, or 4.")



menu(packages_hash, truck_list)