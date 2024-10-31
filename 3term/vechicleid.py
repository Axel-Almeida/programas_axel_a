vehicles = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
        }

def display_vin(search):
    if search in vehicles:
        vin:list=vehicles[search]
        print(" ")
        print("Vehicle Information Number.\n")
        print(f"VIN: {search}")
        print(f"Year: {vin[0]}")
        print(f"Manufacturer: {vin[1]}")
        print(f"Model: {vin[2]}")
        print(f"Color: {vin[3]}")
        print(f"Engine Design: {vin[4]}")
        print(f"Engine Displace: {vin[5]}")
        print(" ")
        main()
    else:
        print(f"{search} is not on the list of vehicles.")
        print(" ")
        main()


def main():
    search=input("Enter the vehicle indentification number (VIN):")
    display_vin(search)

if __name__ == "__main__":
    main()