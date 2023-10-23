import csv
import json

# Load JSON data from a file
with open('Nigeria.json', 'r') as json_file:
    data = json.load(json_file)

# Initialize CSV files
country_csv = open('country.csv', 'w', newline='')
region_csv = open('region.csv', 'w', newline='')
city_csv = open('city.csv', 'w', newline='')

country_writer = csv.writer(country_csv)
region_writer = csv.writer(region_csv)
city_writer = csv.writer(city_csv)

# Write headers for CSV files
country_writer.writerow(["country_name", "longitude",
                        "latitude", "number_of_regions", "country_id"])
region_writer.writerow(["country_name", "region_name",
                       "longitude", "latitude", "number_of_cities" ,"region_id"])
# region_writer.writerow(["region name", "region ID"])
city_writer.writerow(["country_name", "region_name",
                     "city_name", "Longitude", "latitude", "city_id"])
# region_writer.writerow(["country name","region name", "longitude", "latitude", "number of cities" "region ID"])

# Initialize country ID
country_id = 2

# Process the JSON data
for country_data in data:
    for country_name, country_info in country_data["countries"].items():
        country_longitude = country_info["longitude"]
        country_latitude = country_info["latitude"]
        country_name = country_info["name"]
        divisions = country_info["divisions"]
        # city = country_info["sub_divisions"]
        num_regions = len(divisions)
        # num_cities = len(city)
    # Write country data to country.csv
        country_writer.writerow(
            [country_name, country_longitude, country_latitude, num_regions, country_id])


    # Process regions
        region_id = 2.01
    
        for division_name, division_info in country_info["divisions"].items():
            region_longitude = division_info["longitude"]
            region_latitude = division_info["latitude"]
            region_name = division_info["name"]
            # divisions = divisions["divisions"]
            for city_name, city_info in division_info["sub_divisions"].items():
                city_name = city_info["name"]

                num_cities = len(city_name)
    
            
            

        # Write region data to region.csv
            region_writer.writerow(
            [country_name, region_name, region_longitude, region_latitude, num_cities, region_id])
# region_writer.writerow(["country name","region name", "longitude", "latitude", "number of cities" "region ID"])
        # Process cities (sub_divisions)
            city_ID = 2.0001
            for city_name, city_info in division_info["sub_divisions"].items():
            # for city_name, city_data in region_data["sub_divisions"].items():
                city_longitude = city_info["longitude"]
                city_latitude = city_info["latitude"]
                city_name = city_info["name"]
                # divisions = divisions["divisions"]
                #city = city_info["sub_divisions"]
                # num_regions = len(divisions)
                num_cities = len(city_name)

                city_writer.writerow(
                    [country_name, region_name, city_name,  city_longitude, city_latitude, city_ID])

                city_ID += 0.0001

            region_id += 0.01

    country_id += 0

# Close CSV files
country_csv.close()
region_csv.close()
city_csv.close()
