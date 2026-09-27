from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

PIN = "4827"
GOOGLE_KEEP = "https://keep.google.com"

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>NoteDrop</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            text-align: center;
            padding-top: 100px;
        }

        .box {
            background: white;
            width: 320px;
            margin: auto;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }

        h1 {
            font-size: 36px;
        }

        input {
            width: 170px;
            padding: 12px;
            font-size: 25px;
            text-align: center;
            letter-spacing: 8px;
        }

        button {
            margin-top: 20px;
            padding: 12px 25px;
            font-size: 18px;
            cursor: pointer;
        }

        .error {
            color: red;
        }
    </style>
</head>

<body>

<div class="box">
    <h1>NoteDrop</h1>

    <p>Enter your 4-digit code</p>

    <form method="POST">
        <input
            type="password"
            name="pin"
            maxlength="4"
            inputmode="numeric"
            required
        >

        <br>

        <button type="submit">Continue</button>
    </form>

    {% if error %}
        <p class="error">Incorrect code.</p>
    {% endif %}
</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        entered_pin = request.form.get("pin")

        if entered_pin == PIN:
            return redirect(GOOGLE_KEEP)

        return render_template_string(PAGE, error=True)

    return render_template_string(PAGE, error=False)


if __name__ == "__main__":
    app.run(debug=True)
