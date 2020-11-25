from my_model import Document, db


class Friend(Document):
    collection = db.friends


class Product(Document):
    collection = db.products


def main():
    # f1 = Friend({
    #     'first_name': 'Anna',
    #     'last_name': 'Svensson',
    #     'friend_rating': 8,
    #     'email': 'anna@email.com'
    # })
    #
    # f1.save()

    # Product.insert_many([
    #     {
    #         'name': 'Book',
    #         'stock': 19
    #     },
    #     {
    #         'name': 'Bike',
    #         'stock': 45
    #     },
    #     {
    #         'name': 'Pen',
    #         'stock': 98
    #     }
    # ])

    #prods = Product.find(**{'name': 'Ball'})
    # prods = Product.all()
    # for item in prods:
    #     print(item)

    prod = Product.find(stock = {'$gt': 1800}).first_or_none()
    print(prod)
    # prod.stock = 15
    # print(type(prod._id))
    # prod.save()
    # prods = Product.all()
    # for item in prods:
    #     print(item)

    #Product.delete(name='Pen')

if __name__ == '__main__':
    main()
