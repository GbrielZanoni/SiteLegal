from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("O site está funcionando corretamente.")
        else:
            print(f"O site retornou um status code {response.status_code}. Pode estar com problemas.")
