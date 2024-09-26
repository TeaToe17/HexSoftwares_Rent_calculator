def calculate_rent():
    accomodation_bill = int(input(" Whats the accomodation bill? "))
    water_bill = int(input(" What's the water bill per year? ")) 
    electricity_bill = int(input(" What's the electricity bill per year? ")) 
    tenants = int(input(" How many tenants? "))
    rent = (accomodation_bill+water_bill+electricity_bill)/tenants
    print(f" The rent for each tenant is ${rent} ")

if __name__ == "__main__":
    calculate_rent()