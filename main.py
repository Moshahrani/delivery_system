# ******************

# Moshfeq Shahrani
# ID - 011919956
# C950 


import csv
import datetime

from hashTable import CustomHashTable
from package import Package
from truck import Truck

#   linear time complexity O(n) due to reading the data, 
#   creating the new package object and assigning the values for each package attribute
#   hash table is also O(n) space complexity as it stores all csv data one time by package   

def loadPackagesFromCSV(filename, hash_table):

    with open(filename) as packages:
        packageData = csv.reader(packages, delimiter=',')
        
        for package in packageData:
            package_id = package[0]
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            delivery_time = package[5]
            weight = package[6]
            status = 'At WGUPS Hub'
            
            newPackage = Package(
                ID=package_id, address=address, city=city, state=state,
                zip_code=zip_code, delivery_time=delivery_time, weight=weight,
                status=status
            )

    with open(filename) as packages:
        packageData = csv.reader(packages, delimiter=',')
        
        #  extracting all attributes and creating a new package Object for each package's data

        for package in packageData:
            package_id = package[0]
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
            else:
                print(f"Package ID {package_id} added successfully.")



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
print(address_data)

# O(1) time complexity, constant time lookup
# method to calculate distance between two addresses
# returns float of measured distance

def distance_between(address1, address2):
    distance = distance_data[address1][address2]

    #  check for reverse in case of blank data
    if distance == '':
        distance = distance_data[address2][address1]
    return float(distance)
