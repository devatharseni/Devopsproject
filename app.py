from flask import Flask

app = Flask(__name__)

def get_count():
    try:
        with open("count.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def update_count():
    count = get_count() + 1
    with open("count.txt", "w") as f:
        f.write(str(count))
    return count

@app.route('/')
def home():
    count = get_count()
    return f"""
    <h1>Visitor Counter App 👥</h1>
    <h2>Total Visitors: {count}</h2>
    <a href='/visit'>Click to Visit</a>
    """

@app.route('/visit')
def visit():
    count = update_count()
    return f"""
    <h2>Thanks for visiting!</h2>
    <h3>Total Visitors: {count}</h3>
    <a href='/'>Go Back</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
