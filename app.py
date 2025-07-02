from flask import Flask, render_template, request
from grade_calculator import calculate_grade, InvalidWeightError

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            assignments = [
                (
                    request.form['name1'],
                    float(request.form['grade1']),
                    float(request.form['weight1'])
                ),
                (
                    request.form['name2'],
                    float(request.form['grade2']),
                    float(request.form['weight2'])
                ),
                (
                    request.form['name3'],
                    float(request.form['grade3']),
                    float(request.form['weight3'])
                )
            ]
            final_grade = calculate_grade(assignments)
            return render_template('index.html', final_grade=final_grade)
        except InvalidWeightError as e:
            return render_template('index.html', error=str(e))
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers for grades and weights.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
