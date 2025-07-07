from flask import Flask, render_template, request
from App.grade_calculator import calculate_grade, InvalidWeightError

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            assignments = []
            for i in range(1, 6):  # Loop through 5 fixed assignments
                name = request.form.get(f'name{i}')
                grade = float(request.form.get(f'grade{i}'))
                weight = float(request.form.get(f'weight{i}'))
                assignments.append((name, grade, weight))

            final_grade = round(calculate_grade(assignments), 2)

            # Prepare calculation breakdown for display
            steps = []
            total_weight = sum(weight for _, _, weight in assignments)
            for name, grade, weight in assignments:
                portion = grade * (weight / 100)
                if total_weight != 100:
                    portion /= (total_weight / 100)
                steps.append({
                    'name': name,
                    'grade': grade,
                    'weight': weight,
                    'portion': round(portion, 2)
                })

            return render_template('index.html',
                                   final_grade=final_grade,
                                   steps=steps,
                                   assignments=assignments)
        except InvalidWeightError as e:
            return render_template('index.html', error=str(e))
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers for grades and weights.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)