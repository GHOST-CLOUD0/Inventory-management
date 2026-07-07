import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response =  requests.get(f"{BASE_URL}/inventory")
    print(response.json())
    
def view_one_inventory_id():
    item_id = input("Enter item ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())
    
def add_new_inventory():
    barcode = input("Barcode")
    name = input("Product name")
    ingredients = input("Ingredients: ")
    brand = input("brand: ")
    try:
        price = float(input("Price: "))
        stock = int(input("stock: "))
    except ValueError:
        print("price must be a number and stock must be a whole number")  
        return  
    payload = {
        "barcode": barcode,
        "name": name,
        "ingredients": ingredients,
        "brand": brand,
        "price": price,
        "stock": stock
    }  
    response = requests.post(f"{BASE_URL}/inventory", json=payload)
    print(response.json())    
    
def update_inventory():
    item_id = input("Enter item ID to update")
    price = input("New price (leave blank to skip): ")
    stock = input("New stock (leave blank to skip): ")
    
    payload = {}
    try:
        if price:
            payload["price"] = float(price)
        if stock:
            payload["stock"] = int(stock)  
    except ValueError:
        print("price must be a  number and stock must be a whole number")        
        
    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=payload)
    if response.status_code == 200:
        print("Product successfully updated!")
        print(response.json())
    
def delete_inventory():
    item_id = input("Enter item ID: ")
    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    if response.status_code == 204:
        print("Item deleted")
    else:    
        print(response.json())
    
def search_openfoodfacts():
    barcode = input("Enter barcode: ")
    response =requests.get(f"{BASE_URL}/product/{barcode}")
    print(response.json()) 
    
def import_products():
    barcode = input("Enter product barcode: ")
    response = requests.post(f"{BASE_URL}/inventory/import",json={"barcode": barcode})
    if response.status_code == 201:
        print("Product import successful!")
        print(response.json())
    elif response.status_code == 404:
        print("Product not found on OpenFoodFacts.") 
    else:
        print("Failed to import product")     
    
def print_menu():
    while True:
        print('\n=====Inventory Management====')
        print('1. View inventory')
        print('2. View one inventory ID')
        print('3. Add new inventory')
        print('4. Update inventory')
        print('5. Delete inventory')
        print('6. Search OpenFoodFacts')
        print('7. Import Products')
        print('8. Exit')
        
        choice = input("Select an option: ")
        
        if choice == "1":
            view_inventory()
        elif choice == "2":
            view_one_inventory_id()  
        elif choice == "3":
            add_new_inventory()      
        elif choice == "4":
            update_inventory()
        elif choice == "5":
            delete_inventory() 
        elif choice == "6":
            search_openfoodfacts()
        elif choice == "7":
            import_products()  
        elif choice == "8":
            break
        else:
            print("Invalid option")    
            
if __name__ == "__main__":
    try:
        print_menu()
    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask API. Make sure the server is running.")                         