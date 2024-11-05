import sqlite3

def initialize_database():
    db_connection = sqlite3.connect('chocolate_house.db')  # Connect to the SQLite database
    db_cursor = db_connection.cursor()

    # Create tables for seasonal flavors, ingredient inventory, and customer feedback
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        season TEXT NOT NULL
    )''')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )''')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        suggestion TEXT NOT NULL,
        allergies TEXT  -- This field holds allergy information
    )''')

    db_connection.commit()  # Save the changes to the database
    db_connection.close()    # Close the database connection

def add_seasonal_flavor(flavor_name, season):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO seasonal_flavors (flavor_name, season) VALUES (?, ?)', (flavor_name, season))
    conn.commit()
    conn.close()

def add_ingredient(ingredient_name, quantity):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)', (ingredient_name, quantity))
    conn.commit()
    conn.close()

def add_customer_feedback(customer_name, suggestion, allergies):
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO customer_feedback (customer_name, suggestion, allergies) VALUES (?, ?, ?)', 
        (customer_name, suggestion, allergies)
    )
    conn.commit()
    conn.close()

def view_seasonal_flavors():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def view_ingredient_inventory():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ingredient_inventory')
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

def view_customer_feedback():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customer_feedback')
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

# Example usage
initialize_database()  # Ensure the database and tables are initialized

# Add some seasonal flavors
add_seasonal_flavor('Pumpkin Spice', 'Fall')
add_seasonal_flavor('Mint Chocolate', 'Winter')

# Add some ingredients to the inventory
add_ingredient('Cocoa Powder', 50)
add_ingredient('Sugar', 100)

# Add customer feedback with allergy concerns
add_customer_feedback('Alice', 'Dark Chocolate Raspberry', 'None')  # No allergies
add_customer_feedback('Bob', 'Peanut Butter Crunch', 'Peanuts')  # Allergy to peanuts
add_customer_feedback('Charlie', 'Milk Chocolate Caramel', 'Dairy')  # Allergy to dairy

# View seasonal flavors
print("Seasonal Flavors:")
flavors = view_seasonal_flavors()
for flavor in flavors:
    print(flavor)

# View ingredient inventory
print("\nIngredient Inventory:")
ingredients = view_ingredient_inventory()
for ingredient in ingredients:
    print(ingredient)

# View customer feedback with allergy concerns
print("\nCustomer Feedback:")
feedback = view_customer_feedback()
for suggestion in feedback:
    customer_name, suggestion_text, allergies = suggestion[1], suggestion[2], suggestion[3]
    allergy_info = f" (Allergies: {allergies})" if allergies and allergies.lower() != 'none' else ""
    print(f"{customer_name} suggested: '{suggestion_text}'{allergy_info}")
