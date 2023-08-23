
# Techno Market - An online store for computers and computer components.
Welcome to Techno Market, a Django application for an online store focused on computers and computer components. This application has two types of users, buyers and sellers, who can register, order products, and also add new products for sale.

Link to the live version of the application: https://stefananevski.pythonanywhere.com/
## Features

* Registration and authentication for both buyers and sellers.
* Buyers can browse a list of products and add them to their cart.
* Buyers can place orders.
* Sellers can add new products for sale.
* The administrator has control over users and products.


## Installation

1. Clone the repository to your local system:

```bash
    git clone https://github.com/anevski-stefan/TehnoMarket
    cd TehnoMarket
```

2. Install the dependencies:

```bash
    pip install -r requirements.txt
```
    
3. Start the server:

```bash
    python manage.py runserver
```   

4. Open the application in your browser:

```bash
    http://127.0.0.1:8000/
```   
## User Instructions:

Log in to the admin panel using the following link:

```bash
    http://127.0.0.1:8000/admin/
```

Use the following credentials to log in as an administrator:

* Username: admin
* Password: admin

In the admin panel, you can assign permissions and manage users and products.

To register new users, use the "Login/Registration" link on the homepage.

Use the links on the site to browse and order products.


