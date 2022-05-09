from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

doc.title.string = "Beautiful Soup Demo"
doc.h1.string = "What is Beautiful Soup"
doc.find("p", "para").string = "Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree."
print(doc.prettify())