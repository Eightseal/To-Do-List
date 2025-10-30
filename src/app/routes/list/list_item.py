from datetime import datetime, timezone

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from ...extensions import db
from ...models import To_Do_List

# Blueprint for index page for routes
list_bp = Blueprint("list_item", __name__, url_prefix="/list", template_folder="templates")


@list_bp.route("/")
def index():
    list_items = db.session.query(
        To_Do_List
    ).all()  # FIXED: Changed variable name to list_items for consistency

    return render_template(
        "list.html", list_items=list_items
    )  # FIXED: Changed list_item to list_items


@list_bp.route("/add_list_item", methods=["GET", "POST"])
def add_list_item():
    # If the form is submitted, create a new user
    if request.method == "POST":
        task_name = request.form.get("task_name")
        to_do = request.form.get("to_do")
        # FIXED: Removed timestamp from form and using current time instead
        timestamp = datetime.now(timezone.utc)

        # Create a new list item
        new_list_item = To_Do_List(task_name=task_name, to_do=to_do, timestamp=timestamp)

        try:
            db.session.add(new_list_item)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            print(error)

        flash(f"List item created successfully: {new_list_item.task_name}")

        # FIXED: Changed "list.index" to "list_item.index"
        return redirect(url_for("list_item.index"))
    return render_template("add_edit_list_item.html")


@list_bp.route("/edit_list_item/<list_item_id>", methods=["GET", "POST"])
def edit_list_item(list_item_id):
    """
    GET: Returns create_user.html
    POST: Creates a new user
    """

    # FIXED: Changed filter syntax from To_Do_List.id to just id
    list_item = db.session.query(To_Do_List).filter_by(id=list_item_id).first()

    if not list_item:
        return abort(404)

    # If the form is submitted, create a new user
    if request.method == "POST":
        task_name = request.form.get("task_name")
        to_do = request.form.get("to_do")
        # FIXED: For editing, we don't change the timestamp, or you might want to add an updated_at field

        list_item.task_name = task_name
        list_item.to_do = to_do

        try:
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            print(error)

        flash(f"List item edited successfully: {list_item.task_name}")

        # FIXED: Changed "list.index" to "list_item.index"
        return redirect(url_for("list_item.index"))

    return render_template("add_edit_list_item.html", list_item=list_item)
