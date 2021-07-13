from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    backgrounds = [
        "https://cdn.glitch.com/d08bb326-e251-4744-9266-f454d653c7c1%2F1.jpg?v=1624806666676",
        "https://cdn.glitch.com/d08bb326-e251-4744-9266-f454d653c7c1%2F2.jpg?v=1624806671981",
        "https://cdn.glitch.com/d08bb326-e251-4744-9266-f454d653c7c1%2F3.jpg?v=1624806699166",
        "https://cdn.glitch.com/d08bb326-e251-4744-9266-f454d653c7c1%2F4.jpg?v=1624806704706",
        "https://cdn.glitch.com/d08bb326-e251-4744-9266-f454d653c7c1%2F5.jpg?v=1624806707766",
        "https://cdn.glitch.com/d08bb326-e251-4744-9266-f454d653c7c1%2F6.jpg?v=1624806710754"
    ]
    return render_template("index.html", backgrounds=backgrounds)

if __name__ == "__main__":
    # Use in replit
    # app.run(host='0.0.0.0', port=8080)

    app.run(host='localhost', debug=True, port=8080)
