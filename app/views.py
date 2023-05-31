from flask import Blueprint, render_template, redirect, url_for, request
import requests

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("main.html")

@views.route("/author.html")
def author():
    return render_template("author.html")

@views.route("/extraction.html")
def extraction():
    return render_template("extraction.html")

@views.route("/products.html")
def products():
    products = products_list
    return render_template("products.html", products=products)

@views.route("/main.html")
def main():
    return redirect(url_for("views.home"))

products_list = []

@views.route("/extraction.html", methods = ["POST", "GET"])
def form():
    if request.method =="POST":
        product_code = request.form["product_code"]
        url = f"https://www.ceneo.pl/{product_code}"
        response = requests.get(url)
        if response.status_code == 200:
            products_list.append(product_code)
            f = open("ProductsList.txt", "a")
            f.write(f"{product_code}\n")
            f.close()
            return redirect(url_for("views.products"))
        else:
            # alert = open("alert.txt", "r")
            # alert = alert.read()
            # alert = "<h1>Uwaga</h1>"
            return render_template("extraction.html", alert="Invalid Product Code")
            # return render_template("extraction.html", alert=alert)


    else:
        return render_template("home.html")