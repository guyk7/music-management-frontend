from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Base API URL for backend
API_BASE_URL = "http://127.0.0.1:5000"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_singer", methods=["GET", "POST"])
def add_singer():
    if request.method == "POST":
        name = request.form["name"]
        genre = request.form["genre"]
        response = requests.post(f"{API_BASE_URL}/singers", json={"name": name, "genre": genre})
        if response.status_code == 200:
            return redirect(url_for("view_singers"))
        else:
            return "Error adding singer", 500
    return render_template("add_singer.html")

@app.route("/singers")
def view_singers():
    response = requests.get(f"{API_BASE_URL}/singers")
    if response.status_code == 200:
        singers = response.json()
        return render_template("singers.html", singers=singers)
    else:
        return "Error fetching singers", 500

@app.route("/singers/<singer_id>/delete", methods=["POST"])
def delete_singer(singer_id):
    response = requests.delete(f"{API_BASE_URL}/singers/{singer_id}")
    if response.status_code == 200:
        return redirect(url_for("view_singers"))
    else:
        return "Error deleting singer", 500

@app.route("/singers/<singer_id>/add_song", methods=["GET", "POST"])
def add_song(singer_id):
    if request.method == "POST":
        title = request.form["title"]
        year = request.form["year"]
        album = request.form["album"]
        response = requests.post(
            f"{API_BASE_URL}/singers/{singer_id}/songs",
            json={"title": title, "year": year, "album": album}
        )
        if response.status_code == 200:
            return redirect(url_for("view_songs", singer_id=singer_id))
        else:
            return "Error adding song", 500
    return render_template("add_song.html", singer_id=singer_id)

@app.route("/singers/<singer_id>/songs")
def view_songs(singer_id):
    response = requests.get(f"{API_BASE_URL}/singers/{singer_id}/songs")
    if response.status_code == 200:
        songs = response.json()
        return render_template("songs.html", singer_id=singer_id, songs=songs)
    else:
        return "Error fetching songs", 500

@app.route("/singers/<singer_id>/songs/<song_id>/delete", methods=["POST"])
def delete_song(singer_id, song_id):
    response = requests.delete(f"{API_BASE_URL}/singers/{singer_id}/songs/{song_id}")
    if response.status_code == 200:
        return redirect(url_for("view_songs", singer_id=singer_id))
    else:
        return "Error deleting song", 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
