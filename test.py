import mysql.connector as conn
db=conn.connect(host="localhost",user="root",password="<YOUR PASSWORD>")
cur= db.cursor()

# Creating database
try:
    cur.execute("use harshap")
except conn.errors.ProgrammingError as err:
    cur.fetchall()
    cur.execute("create database harshap;")

cur.execute("use harshap")
cur.fetchall()

try:
    cur.execute("select * from products")
except conn.errors.ProgrammingError as err:
    cur.execute("""CREATE TABLE products (
    product_id     INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(255) NOT NULL,
    brand         VARCHAR(255),
    category      VARCHAR(255),
    price         DECIMAL(10,2) NOT NULL,
    currency      VARCHAR(10) DEFAULT 'INR',
    weight        DECIMAL(10,2),
    unit          VARCHAR(50),
    ingredients   TEXT,
    allergens     VARCHAR(255),
    calories      INT,
    protein       DECIMAL(10,2),
    carbohydrates DECIMAL(10,2),
    fats          DECIMAL(10,2),
    sugar         DECIMAL(10,2),
    fiber         DECIMAL(10,2),
    sodium        DECIMAL(10,2),
    availability  INT DEFAULT 0
);
""")

def inserting_ini_values():
    cur.fetchall()
    try:   
        products_list=[
            (1, "Organic Almond Butter", "Nutty Delights", "Nut Butters", 12.99, "INR", 250, "g", 
            "Almonds, Sea Salt", "Nuts", 180, 6, 7, 15, 2, 3, 120,10),

            (2, "Whole Grain Oats", "Healthy Foods", "Cereals", 5.49, "INR", 500, "g", 
            "Whole grain oats", "Gluten", 150, 5, 27, 3, 1, 4, 0,10),

            (3, "Greek Yogurt - Vanilla", "Dairy Fresh", "Dairy", 3.99, "INR", 150, "ml", 
            "Milk, Vanilla Extract, Live Cultures", "Dairy", 120, 10, 12, 4, 8, 0, 50,10),

            (4, "Dark Chocolate 85%", "Choco Luxe", "Snacks", 4.29, "INR", 100, "g", 
            "Cocoa Mass, Cocoa Butter, Sugar", "None", 200, 4, 15, 14, 10, 3, 5,10),

            (5, "Avocado Oil", "Nature's Choice", "Oils", 9.99, "INR", 500, "ml", 
            "Avocado Oil", "None", 120, 0, 0, 14, 0, 0, 0,10),

            (6, "Quinoa - Organic", "Super Foods", "Grains", 8.99, "INR", 400, "g", 
            "Organic Quinoa", "None", 220, 8, 39, 4, 1, 5, 5,10),

            (7, "Chia Seeds", "Nutri Boost", "Superfoods", 6.79, "INR", 300, "g", 
            "Chia Seeds", "None", 130, 6, 12, 9, 0, 10, 2,10),

            (8, "Coconut Water", "Tropical Bliss", "Beverages", 2.49, "INR", 330, "ml", 
            "Coconut Water", "None", 60, 1, 15, 0, 12, 1, 40,10),

            (9, "Cashew Butter", "Nutty Delights", "Nut Butters", 11.49, "INR", 250, "g", 
            "Cashews, Sea Salt", "Nuts", 190, 5, 8, 16, 2, 3, 125,10),

            (10, "Organic Honey", "Bee Pure", "Sweeteners", 7.99, "INR", 500, "ml", 
            "Raw Honey", "None", 80, 0, 21, 0, 20, 0, 2,10),

            (11, "Peanut Butter - Crunchy", "NutriNuts", "Nut Butters", 10.49, "INR", 250, "g", 
            "Peanuts, Sea Salt", "Nuts", 190, 7, 6, 16, 2, 3, 120,10),

            (12, "Matcha Green Tea Powder", "Zen Tea", "Beverages", 14.99, "INR", 100, "g", 
            "Organic Matcha Tea", "None", 10, 1, 2, 0, 0, 1, 0,10),

            (13, "Almond Milk - Unsweetened", "Dairy Free", "Dairy Alternatives", 3.99, "INR", 1000, "ml", 
            "Almonds, Water", "Nuts", 30, 1, 2, 2, 0, 0, 120,10),

            (14, "Pumpkin Seeds", "Healthy Bites", "Snacks", 5.99, "INR", 200, "g", 
            "Pumpkin Seeds", "None", 180, 8, 4, 14, 1, 3, 10,10),

            (15, "Brown Rice", "Eco Grains", "Grains", 6.49, "INR", 1000, "g", 
            "Whole Grain Brown Rice", "None", 215, 5, 45, 2, 1, 4, 0,10),
        ]

        # Entring Values for the products
        for i in products_list:
            cur.execute(f"insert into products values {i}")
            cur.fetchall()
        db.commit()
    except conn.errors.IntegrityError:
        return "The database is already existing and the initial values have been added"

def inserting_single_values(values:list):
    if len(values[0])!=18:
        return "The required column length is not satisfied."
    else:
        try:
            cur.fetchall()
            cur.execute(f"insert into products values{values[0]}")
            db.commit()
        except conn.errors.IntegrityError as err:
            return err
    

product= [(
    16, "Protein Bar - Chocolate", "Fit Snacks", "Snacks", 2.99, "USD", 60, "g", 
    "Whey Protein, Cocoa, Almonds, Honey", "Dairy, Nuts", 220, 15, 20, 8, 10, 5, 80,23
)]


print(inserting_single_values(product))
