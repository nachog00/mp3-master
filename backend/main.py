from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the path to the USB drive
usb_drive_path = "/path/to/usb/drive"

@app.route("/")
def index():
    # Get the list of MP3 files on the USB drive
    mp3_files = [file for file in os.listdir(usb_drive_path) if file.endswith(".mp3")]
    return render_template("index.html", mp3_files=mp3_files)

@app.route("/upload", methods=["POST"])
def upload():
    # Check if a file was uploaded
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]

    # Save the uploaded file to the USB drive
    file.save(os.path.join(usb_drive_path, file.filename))

    return redirect(url_for("index"))

@app.route("/delete/<filename>")
def delete(filename):
    # Delete the specified file from the USB drive
    file_path = os.path.join(usb_drive_path, filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)