from flask import Flask, render_template, redirect, request

app = Flask(__name__)

ALL_DATA = [
    {
        'f_name': 'Mubashir',
        'l_name': 'Haider',
        'class': 'BSCS', 'dofbirth':
        '28/10/2003',
        'roll': '1',
        'fee': '25000'
    },
    {
        'f_name': 'Ali Raza',
        'l_name': 'Yameen',
        'class': 'BBA',
        'dofbirth':
        '5/10/2000',
        'roll': '2',
        'fee': '35000'
    },
    {
        'f_name': 'Usman',
        'l_name': 'Malik',
        'class': 'BSCS',
        'dofbirth': '26/10/2002',
        'roll': '3',
        'fee': '12000'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/student.list")
def student_list():
    return render_template("student_list.html", students=ALL_DATA)


@app.route("/student/<roll_number>")
def student_detail(roll_number):
    for student in ALL_DATA:
        if student['roll'] == roll_number:
            return render_template("student_detail.html", student=student)
    return render_template("404.html")


@app.route("/student/<roll_number>/delete")
def delete_student(roll_number):
    for student in ALL_DATA:
        if student['roll'] == roll_number:
            ALL_DATA.remove(student)
            return redirect("/student.list")
    return render_template("404.html")

@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    print(request.method) # GET, POST
    if request.method == "GET":
        return render_template("add_student.html")
    elif request.method == "POST":
        
        first_name =  request.form["first_name"]
        last_name = request.form["last_name"]
        class_ = request.form["class"]
        dob_ = request.form["date_of_birth"]
        roll_ = request.form["roll_number"]
        fees_ = request.form["fee"]
        student = {
            'f_name': first_name,
            'l_name': last_name,
            'class': class_,
            'dofbirth': dob_,
            'roll': roll_,
            'fee': fees_
            }

        ALL_DATA.append(student)
        return redirect("/student.list")


@app.route("/student/<roll_number>/edit", methods=['GET', 'POST'])
def edit_student(roll_number):
    # Handle 404/ Check if students exists
    current_student = None
    for student in ALL_DATA:
        if student['roll'] == roll_number:
            current_student = student
    if current_student == None:
        return render_template("404.html")
    
    # Send the form on get request
    if request.method == "GET":
        return render_template("edit_student.html", student=current_student)
    elif request.method == 'POST':
        index = ALL_DATA.index(current_student)
        ALL_DATA[index] = {
            "roll": roll_number,
            "f_name": request.form["first_name"],
            "l_name": request.form["last_name"],
            "class": request.form["class"],
            "dofbirth": request.form["date_of_birth"],
            "fee": request.form["fee"],
        }
        return redirect("/student.list")

