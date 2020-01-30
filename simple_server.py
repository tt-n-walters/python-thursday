from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    args = list(request.args.lists())
    if len(args) > 0:
        return "You sent: " + str(", ".join([arg[0] for arg in args]))
    else:
        return "Hi! Welcome to my amazing Python server."


@app.route("/login")
def login():
    args_keys = request.args.keys()
    if "username" in args_keys:
        if "password" in args_keys:
            username = request.args.get("username")
            password = request.args.get("password")
            if username == "admin":
                if password == "strongestpasswordever":
                    return "Logged in correctly!"
                else:
                    return "Incorrect password."
            else:
                return "Invalid username."
        else:
            return "Password not given."
    else:
        return "Username not given."



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6660, debug=True)
