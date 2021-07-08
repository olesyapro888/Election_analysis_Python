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
  print(f'{county} county has {voters:,} registered voters')

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

for countty in voting_data:
  for vots in countty.values():
    print (countty['county'], vots['registered_voters'])

# The same but using range()
#for county in range(len(voting_data)):
    #print(voting_data[county]['county'])

# To get values from a list of Dict. Needs to use Nested loop
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

# Print with thousands separator
#for county, voters in counties_dict.items():
  #print(f'{oting_data[county]['county']} county has {oting_data[county]['county']:,} registered voters')

#for county in range(len(voting_data)):
  #print(voting_data[county]['registered_voters'])
  
  #print(voting_data[county]['county'] + " county has " + str(voting_data[county]['registered_voters']) + " registered voters.") #string is imp to apply ,thous...separator)
