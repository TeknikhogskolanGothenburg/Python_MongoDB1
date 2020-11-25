from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://root:s3cr37@localhost:27016')
    db = client.store_db

    db.strunt.insert_one({
        'product_name': 'Diamond Ring',
        'items_in_stock': 11,
        'Carat': 18
    })

    products = db.products.find({})

    for product in products:
        print(product)


if __name__ == '__main__':
    main()
