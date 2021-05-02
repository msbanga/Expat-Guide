from project import app
import os


if __name__ == '__main__':  # on running python app.py
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)
