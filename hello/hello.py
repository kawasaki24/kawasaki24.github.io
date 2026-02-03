import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://forums.redflagdeals.com/hot-deals-f9/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    headers = soup.find_all("a", class_="thread_title_link")

    threads = []
    thread_dict = {}

    for header in headers:
        thread_dict = {
            "title": header.get_text(strip=True),
            "url": header["href"]
        }

        threads.append(thread_dict)

    return render_template("rfd.html", threads=threads)

