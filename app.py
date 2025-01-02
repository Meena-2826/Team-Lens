from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS       #cross orgin resource sharing

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for API testing

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pooja@1234'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'teamlens'

mysql = MySQL(app)

# Routes for rendering HTML templates
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-employee')
def add_employee_page():
    return render_template('add_employee.html')

@app.route('/assign-task')
def assign_task_page():
    return render_template('assign_task.html')

@app.route('/view-tasks')
def view_tasks_page():
    return render_template('view_tasks.html')

# API Endpoint: Add employee
@app.route('/manager/add-employee', methods=['POST'])
def add_employee():
    try:
        data = request.form
        name = data['name']
        email = data['email']
        skills = data['skills']
        
        conn = mysql.connection
        cursor = conn.cursor()
        query = "INSERT INTO employees (name, email, skills) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, skills))
        conn.commit()
        return jsonify({"message": "Employee added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Assign task
@app.route('/manager/assign-task', methods=['POST'])
def assign_task():
    try:
        data = request.form
        employee_id = data['employee_id']
        task_description = data['task_description']
        deadline = data['deadline']
        
        conn = mysql.connection
        cursor = conn.cursor()
        query = "INSERT INTO tasks (employee_id, task_description, deadline) VALUES (%s, %s, %s)"
        cursor.execute(query, (employee_id, task_description, deadline))
        conn.commit()
        return jsonify({"message": "Task assigned successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: View employee performance
@app.route('/manager/view-performance', methods=['GET'])
def view_performance():
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        query = """
        SELECT employees.name, employees.skills, tasks.task_description, 
               performance.time_spent, performance.performance_score
        FROM employees
        JOIN tasks ON employees.id = tasks.employee_id
        JOIN performance ON tasks.id = performance.task_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        results = [
            {
                "employee_name": row[0],
                "skills": row[1],
                "task_description": row[2],
                "time_spent": row[3],
                "performance_score": row[4],
            }
            for row in rows
        ]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint: Employee tasks
@app.route('/employee/view-tasks/<int:employee_id>', methods=['GET'])
def view_tasks(employee_id):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        query = "SELECT task_description, deadline FROM tasks WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        rows = cursor.fetchall()
        
        tasks = [{"task_description": row[0], "deadline": row[1]} for row in rows]
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
