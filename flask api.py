from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Resume Home Page</title>
        <style>
            body{
                margin:0;
                font-family:Arial, Helvetica, sans-serif;
                background:#f4f6f9;
                color:#222;
            }
            header{
                background:#1a73e8;
                color:#fff;
                padding:20px;
                font-size:26px;
                font-weight:600;
            }
            .container{
                max-width:900px;
                margin:40px auto;
                background:#fff;
                padding:30px;
                border-radius:12px;
                box-shadow:0 4px 16px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <header>My Resume</header>

        <div class="container">
            <h1>Your Name</h1>
            <p>Web Developer | Python Developer | Student</p>
            <h2>Skills</h2>
            <ul>
                <li>Python</li>
                <li>Flask</li>
                <li>HTML / CSS</li>
            </ul>
        </div>

    </body>
    </html>
    """

@app.route("/about")
def abouta():
    return """
    <h1> I am About Page </h1>
    <h2> I am Running in Flask </h2>
    """

if __name__ == '__main__':
    app.run(debug=True)
