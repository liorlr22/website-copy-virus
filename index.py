from flask import Flask, render_template, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')
URL = "https://www.techwithtim.net"
file = r"templates/website.html"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

if __name__ == "__main__":
    @app.route("/")
    def index():
        btn_start = [soup.find('span', {"id": None})]
        btn_start[-1].replace_with("download now")

        for a in soup.findAll('a', attrs={"class": "ow-icon-placement-right ow-button-hover"}):
            a['href'] = "download"
        with open(file, "wb") as f_output:
            f_output.write(soup.prettify("utf-8"))
        return render_template("website.html")

    @app.route("/download")
    def download():
        return render_template("download_file.html")
    app.run(debug=True)
