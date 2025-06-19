from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return '''
        <h2>Feedback Form</h2>
        <form method="POST" action="/submit">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Feedback: <br><textarea name="feedback" rows="4" cols="40"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']

    # Save to file
    with open("feedback_data.txt", "a") as f:
        f.write(f"{name},{email},{feedback}\n")

    return f"<h2>Thank you, {name}!</h2><p>Your feedback has been saved.</p>"



@app.route('/feedbacks', methods=['GET'])
def view_feedbacks():
    try:
        with open("feedback_data.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    # Format the lines into HTML
    formatted = "<h2>Submitted Feedbacks:</h2><ul>"
    for line in lines:
        name, email, feedback = line.strip().split(",", 2)
        formatted += f"<li><strong>{name}</strong> ({email}): {feedback}</li>"
    formatted += "</ul>"

    return formatted


if __name__ == '__main__':
    app.run(debug=True)
