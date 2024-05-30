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
            key = package[0]
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
print(packages_hash)







