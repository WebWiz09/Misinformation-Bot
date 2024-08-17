from flask import Flask, render_template
from features.daily_fact.routes import daily_fact_bp
from features.study_guide.routes import study_guide_bp
from features.fact_checker.routes import fact_checker_bp
from features.source_analyzer.routes import source_analyzer_bp
from features.quiz.routes import quiz_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(daily_fact_bp)
app.register_blueprint(study_guide_bp)
app.register_blueprint(fact_checker_bp)
app.register_blueprint(source_analyzer_bp)
app.register_blueprint(quiz_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
