import requests
import time
from flask import Flask, render_template

def visit_page(url, interval_seconds):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Visited {url} successfully.")
            else:
                print(f"Failed to visit {url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while visiting {url}: {e}")
        
        time.sleep(interval_seconds)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('odpocet.html')

if __name__ == "__main__":
    page_url = "https://silverapp-44ac03b736c2.herokuapp.com/login"
    visit_interval_seconds = 10  # Zmeňte na požadovaný interval v sekundách (napr. 600 sekúnd = 10 minút)

    # Spustíme funkciu pre návštevu stránky v samostatnom vlákne, aby neblokovala spustenie aplikácie Flask
    import threading
    t = threading.Thread(target=visit_page, args=(page_url, visit_interval_seconds))
    t.start()

    # Spustíme aplikáciu Flask
    app.run(debug=True)
