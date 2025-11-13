from flask import Flask, render_template_string

app = Flask(__name__)

# HTML + CSS inline para una página bonita
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Bonita</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: rgba(0, 0, 0, 0.5);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        a {
            display: inline-block;
            padding: 10px 20px;
            background: #ff4b2b;
            color: #fff;
            text-decoration: none;
            border-radius: 10px;
            transition: 0.3s;
        }
        a:hover {
            background: #ff416c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Bienvenido!</h1>
        <p>Esta es una página de ejemplo creada con Flask.</p>
        <a href="#">Haz algo genial</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    # Ejecuta en el puerto 80
    app.run(host="0.0.0.0", port=80, debug=True)
