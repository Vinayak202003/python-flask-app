from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Docker App</title>
        <style>
            * { box-sizing: border-box; }
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 24px;
                background: #0f172a;
                color: #f8fafc;
                font-family: Arial, Helvetica, sans-serif;
            }
            main {
                max-width: 720px;
                width: 100%;
                padding: 48px 32px;
                text-align: center;
                background: #1e293b;
                border: 1px solid #334155;
                border-radius: 18px;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
            }
            .tag {
                display: inline-block;
                padding: 8px 14px;
                border-radius: 999px;
                background: #0c4a6e;
                color: #bae6fd;
                font-size: 13px;
                letter-spacing: 1px;
                text-transform: uppercase;
            }
            h1 {
                margin: 24px 0 16px;
                color: #38bdf8;
                font-size: clamp(30px, 5vw, 44px);
            }
            p {
                color: #cbd5e1;
                font-size: 17px;
                line-height: 1.7;
            }
            footer {
                margin-top: 28px;
                color: #94a3b8;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <main>
            <span class="tag">Python · Flask · Docker</span>
            <h1>Flask App, Dockerized!</h1>
            <p>Built with Python. Powered by Docker.</p>
            <p>Containerized and ready to deploy.</p>
            <footer>Learning and building with DevOps, one container at a time.</footer>
        </main>
    </body>
    </html>
    """


if __name__ == "__main__":
    # Listen on all interfaces so Docker can publish the container port.
    app.run(host="0.0.0.0", port=5000)
