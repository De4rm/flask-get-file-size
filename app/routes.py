import os
from flask import jsonify, render_template, redirect, request
from werkzeug.utils import secure_filename

from app import app
from app.forms import FileForm

size = 0

@app.route("/", methods=["GET","POST"])
def index():
	form = FileForm()
	print(form.validate_on_submit())
	if form.validate_on_submit():
		global size
		f = form.file_upload.data
		file_name = secure_filename(f.filename)
		path_file = os.path.join(app.instance_path, file_name)
		f.save(path_file)
		size = os.path.getsize(path_file)
		os.remove(path_file)

		return redirect('/show_size')


	return render_template("index.html",form=form)

@app.route('/show_size')
def show_size():
	return jsonify({"size": size})
