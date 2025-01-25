from flask import Flask, render_template, request, redirect, url_for
import neopixel_control

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML page with buttons

@app.route('/command', methods=['POST'])
def command():
    cmd = request.form['command']
    if cmd == 'on':
        neopixel_control.turn_on()
    elif cmd == 'off':
        neopixel_control.turn_off()
    elif cmd == 'blink':
        neopixel_control.blink()
    elif cmd == 'color_cycle':
        neopixel_control.color_cycle()
    
    # Redirect back to the main page after the command is executed
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
