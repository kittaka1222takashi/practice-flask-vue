from flask import Blueprint, request, render_template
import os, sys, requests

from flask import request, redirect, url_for, render_template, flash
from backend import app, db
from backend.models import Task

router = Blueprint('app', __name__,
                    template_folder='templates',
                    static_folder='templates/static')

@router.route('/')
def show_entries():
    task = Task.query.order_by(Task.id.desc()).all()
    return render_template('show_entries.html', task=task)

@router.route('/add', methods=['POST'])
def add_entry():
    task = Task(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(task)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('app.show_entries'))

