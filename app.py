from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/ip')  
def get_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"IP Pengunjung: {ip}")
    return f"Your IP is {ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
