from flask import Blueprint,render_template,request,flash
from flask_login import login_required,current_user
from models import Note
from . import db


views = Blueprint("views",__name__)

@views.route('/',methods = ['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)==0:
            flash('Note is Empty',category='error')
        else:
            new_note = Note(data = note,user_id = current_user.id)
            db.session.added(new_note)
            db.session.commit()
            flash('Note Added',category='success')

    return render_template("home.html",user =current_user)

@views.route('delete-note',method='POST')
def delete_node():
    id = request.json['note']
    note = Note.query.get(id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return {}