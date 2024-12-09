items ={"Amul" : {"banana" : 50, "cherry" : 60,"blackberry": 80}, 
        "Cornetto": {"strawberry": 150, "vannilla": 200, "butterscotch": 250}}

cart = {}


def search(query):
    result = []
    icecreams = {}
    for temp, icecream in items.items():
            icecreams.update(icecream)

    for icecream in icecreams:
        if icecream.startswith(query):
            result.append((icecream, icecreams[icecream]))
    
    return result

def filterby(filters):
    result = []
    icecreams = {}
    brands = []
    for brand , icecream in items.items():
            icecreams.update(icecream)
            brands.append(brand)
        
    if filters.lower() == 'price':
        print("\n1) Less than \n2) Equal to \n3) Greater than \n")
        filters = int(input("Apply Filters : "))

        if filters == 1:
            number = int(input("Less than by ? "))
            for icecream in icecreams:
                if icecreams[icecream] < number:
                    result.append((icecream, icecreams[icecreams]))
        elif filters == 2:
            number = int(input("Equal than by ? "))
            for icecream in icecreams:
                if icecreams[icecream] < number:
                    result.append((icecream, icecreams[icecreams]))
        elif filters == 3:
            number = int(input("Greater than by ? "))
            for icecream in icecreams:
                if icecreams[icecream] < number:
                    result.append((icecream, icecreams[icecreams]))
        else:
            print("Valid options ,\n1. Less than\n2. Equal to\n3. Greater than ")
    elif filters.lower() == "brand":
        print(brands)
        
        brand_name = input("Which brand do you want? ").strip().title()
        for item in items:
            if item == brand_name:
                result.append(items[item])
        
        if not result:
            print("No results found")
    else:
        print("Please enter a valid filter , either 'Price' or 'Brand' ")

    if not result:
        print("Results Not Found")

    
    


def add_to_cart(item):

    if item not in cart:
        cart[item] = 1
    else:
        cart[item] +=1

    print("Items added to cart")

def print_cart():
    print("Items in the cart")
    for i in cart:
        print(i, cart[i])
    

def main():
    print("<-------------Welcome to Ice Cream Palor------------> ")
    print("List of available Options: \n 1) Show me the available flavors. \n 2) Search and Filter. \n 3) Add Allergens.")

    option = int(input("Select your Options pls: "))

    if option == 1:

        for item in items:
            print(f"{item} -> {list(items[item])}")

        while True:
            to_buy = input("Please Select One From the Available Flavors: ").strip().lower()
            add_to_cart(to_buy)
            if input("Do you want anything else? ").strip().lower() == "no":
                break        
        print_cart()
    elif option == 2:
        choice = input("Do you want to search or filter? ").strip().lower()
        if choice.lower() == "search":
            query = input("Enter the keyword: ")
            print("Your search result", search(query))
        elif choice.lower() == "filter":
            filters = input("1) Filter by price. \n2) Filter by brand. \n Select your option: ").strip().lower()
            filterby(filters) 
        else:
            print("Please either enter the 'search' or 'filter' ")


if __name__ == "__main__":
    main()