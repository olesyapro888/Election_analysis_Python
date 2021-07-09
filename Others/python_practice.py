#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
 # print(counties[1])

#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")

#for county in counties:
   # print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Print with thousands separator
for county, voters in counties_dict.items():
  print(f'1. {county} county has {voters:,} registered voters')

#Iterate Through a Dictionary
  # Get the Keys of a Dictionary

#for county in counties_dict.keys():
    #print(county)
#for voters in counties_dict.values():
    #print(voters)

#same for values: dict_name[key]
#for county in counties_dict:
   #print(counties_dict[county])

# Get the Values of a Dictionary with .get(key)
#for county in counties_dict:
    #print(counties_dict.get(county))

# Get the Key-Value Pairs of a Dictionary
  # .item() method

#for county, voters in counties_dict.items():
    #print(f'{county} county has {voters} registered voters')

#Iterate Through a List of Dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #print(county_dict)

# The same but using range()
#for county in range(len(voting_data)):
    #print(voting_data[county]['county'])

# To get values from a list of Dict. Needs to use Nested loop
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

# Print with thousands separator

for county in range(len(voting_data)):
  #print(voting_data[county]['registered_voters'])
  
  print(f'2. {voting_data[county]["county"]} county has {voting_data[county]["registered_voters"]:,} registered voters') #string is imp to apply ,thous...separator)

#Print the values of the "roads" key from the nested dictionary.

nested_dict = {"Dakar":{"weather":"sunny", "roads":"dry"}}
ans_1 = nested_dict["Dakar"]["roads"]
print("3. " + ans_1)

#while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 12"

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#Besides being the counter i is being used as the index throughout the list and 
# lst[i]  is the value of elements in the list at index: i

q = 0
while q < len(lst):
    if lst[q] == 100:
        print("There is a 100 at index no: " + str(q))
    q = q+1

#break statement in the for loop so that it prints from 0 to 7 only (including 7).
for s in range(100):
    print(s)
    if s==7:
        break 

#continue statement to the loop so that it skips when iterator equals "sun
weather=["snow", "rain", "sun", "clouds"]

for i in weather:
    if i == "sun":
        continue
    print(i)
