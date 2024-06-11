# app.py

from flask import Flask, render_template, request, redirect
from db import Mysql

app = Flask(__name__)
# Number of data displayed per page
PAGE_SIZE = 2


def page_fun(results,page):

    # Calculate the starting and ending indexes
    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE
    # Get data for the current page
    current_data = results[start_index:end_index]
    # Calculate the total number of pages
    total_pages = len(results) // PAGE_SIZE + (1 if len(results) % PAGE_SIZE > 0 else 0)
    return  current_data, total_pages

@app.route("/", methods=['GET', 'POST'])
def select():
    print("query")
    db = Mysql()
    results = db.getdata()
    # Get the current page number
    page = int(request.args.get('page', 1))
    current_data, total_pages=page_fun(results,page)
    print("current page:",page,"\n")
    return render_template("select.html", results =current_data,page=page, total_pages=total_pages)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    print("delete app")

    id_to_delete = int(request.form['id'])
    # print("=== ",id_to_delete)
    db = Mysql()
    db.delete_data(id_to_delete)
    results = db.getdata()
    page = int(request.args.get('page', 1))  # 获取当前页码
    current_data, total_pages = page_fun(results, page)
    return render_template("select.html", results =current_data,page=page, total_pages=total_pages)

@app.route("/submit_insert",methods=['GET', 'POST'])
def submit_insert():
    print("insert app")

    sub=request.form['sub']
    sub_type=request.form['sub_type']
    subc = request.form['sc']
    relation = request.form['relation']
    obj = request.form['obj']
    ob_type = request.form['obj_type']
    oc=request.form['oc']
    pmid=request.form['pmid']
    sentence = request.form['sentence']
    data = {

            'sub': sub,
            'sub_type': sub_type,
            'sc': subc,
            'relation':relation,
            'obj':obj,
            'obj_type':ob_type,
            'oc':'oc',
            'pmid':pmid,
            'sentence':sentence
    }

    db = Mysql()
    db.insert_data(data)
    results = db.getdata()
    page = int(request.args.get('page', 1))  # 获取当前页码
    current_data, total_pages = page_fun(results, page)
    return render_template("select.html", results =current_data,page=page, total_pages=total_pages)
    # return redirect('select.html')


@app.route("/submit_update", methods=['GET', 'POST'])
def submit_update():

    id_to_update = int(request.form['id'])
    sub = request.form['sub']
    sub_type = request.form['sub_type']
    subc = request.form['sc']
    relation = request.form['relation']
    obj = request.form['obj']
    ob_type = request.form['obj_type']
    oc = request.form['oc']
    sentence = request.form['sentence']
    data = {
        'id':id_to_update,
        'sub': sub,
        'sub_type': sub_type,
        'sc': subc,
        'relation': relation,
        'obj': obj,
        'obj_type': ob_type,
        'oc': oc,
        'sentence': sentence
    }
    db = Mysql()
    db.update_data(id_to_update, data)
    results = db.getdata()

    page = int(request.args.get('page', 1))  # 获取当前页码
    print("update page：",page)
    current_data, total_pages = page_fun(results, page)
    
    return render_template("select.html", results =current_data, page=page, total_pages=total_pages)
     

if __name__ == "__main__":
    app.run( port=5001, host='127.0.0.1')
    # app.run(port=5000, host='0.0.0.0' )
