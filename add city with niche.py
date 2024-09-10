# Input file names
city_file = 'city.txt'
niche_file = 'niche.txt'
output_file = 'output.txt'

# Read data from files
with open(city_file, 'r') as city_f, open(niche_file, 'r') as niche_f:
    cities = city_f.readlines()
    niches = niche_f.readlines()

# Clean and process the data
cities = [city.strip() for city in cities]
niches = [niche.strip() for niche in niches]

# Write the combined data to output file (niche-wise)
with open(output_file, 'w') as output_f:
    for niche in niches:
        for city in cities:
            output_f.write(f"{niche} in {city}\n")

print(f"Data written to {output_file} successfully!")
