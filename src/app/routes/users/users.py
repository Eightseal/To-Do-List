from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from ...extensions import db
from ...models import User

# Blueprint for index page for routes
users_bp = Blueprint("users", __name__, url_prefix="/users", template_folder="templates")


@users_bp.route("/")
def index():
    users = db.session.query(User).all()

    return render_template("users.html", users=users)


@users_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    # If the form is submitted, create a new user
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")

        # Create a new user
        user = User(username=username, email=email)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            print(error)

        flash(f"User created successfully: {user.username}")

        # Redirect to the index page after create
        return redirect(url_for("users.index"))
    return render_template("add_edit_user.html")


@users_bp.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """
    GET: Returns create_user.html
    POST: Creates a new user
    """

    user = db.session.query(User).filter(User.id == user_id).first()

    if not user:
        return abort(404)

    # If the form is submitted, create a new user
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")

        user.username = username
        user.email = email

        # Remove any roles that are no longer selected

        try:
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            print(error)

        flash(f"User Edited successfully: {user.username}")

        # Redirect to the index page after create
        return redirect(url_for("users.index"))

    return render_template("add_edit_user.html", user=user)


@users_bp.route("/toggle_active/<user_id>")
def toggle_active(user_id):
    # Get question
    user = db.session.query(User).filter(User.id == user_id).first()

    if not user:
        flash("User does not exist")
        return redirect(url_for("users.index"))

    user.active = not user.active

    try:
        db.session.commit()
        flash(f"Company toggled {'Active' if user.active else 'Inactive'}")
    except Exception as error:
        db.session.rollback()

        return redirect(url_for("users.index"))

    return redirect(url_for("users.index"))
