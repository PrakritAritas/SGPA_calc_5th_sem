from flask import Flask, render_template, request
from sgpa_calculator import calculate_sgpa

app = Flask(__name__)

# Define route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route to handle form submission and calculate SGPA
@app.route('/calculate_sgpa', methods=['POST'])
def calculate():
    subject_marks = {}
    for subject in request.form:
        subject_marks[subject] = int(request.form[subject])
    sgpa = calculate_sgpa(subject_marks)
    if sgpa is not None:
        return render_template('result.html', sgpa=round(sgpa, 2))
    else:
        return "Error: Unable to calculate SGPA."

if __name__ == '__main__':
    app.run(debug=True)
