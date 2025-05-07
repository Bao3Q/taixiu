from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)
    result = "Tài" if total >= 11 else "Xỉu"
    user_bet = request.json.get('bet')
    win = (user_bet == result)
    return jsonify({
        'dice': dice,
        'total': total,
        'result': result,
        'win': win
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)