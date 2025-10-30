from dotenv import load_dotenv

from src.app import create_app

load_dotenv()

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
