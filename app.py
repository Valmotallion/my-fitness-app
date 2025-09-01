import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

workouts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        workout_name = request.form.get("workout")
        duration_str = request.form.get("duration")

        if not workout_name or not duration_str:
            flash("Please enter both a workout name and a duration.")
        else:
            try:
                duration = int(duration_str)
                workouts.append({"workout": workout_name, "duration": duration})
                flash(f"Successfully added: {workout_name} - {duration} minutes.")
            except ValueError:
                flash("Duration must be a number.")

        return redirect(url_for("index"))

    return render_template("index.html", workouts=workouts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
