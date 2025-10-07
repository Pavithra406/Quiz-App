from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "C++", "Java", "All of these"],
        "answer": "All of these"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        results = []
        for i, q in enumerate(questions):
            selected = request.form.get(f"q{i}")
            correct = q["answer"]
            results.append({
                "question": q["question"],
                "selected": selected,
                "correct": correct,
                "is_correct": selected == correct
            })
            if selected == correct:
                score += 1
        return render_template("result.html", score=score, total=len(questions), results=results)
    
    indexed_questions = list(enumerate(questions))
    return render_template("quiz.html", indexed_questions=indexed_questions)

if __name__ == "__main__":
    app.run(debug=True)
