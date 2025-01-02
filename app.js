function showManagerLogin() {
    document.getElementById('managerLogin').style.display = 'block';
    document.getElementById('login').style.display = 'none';
  }
  
  function showEmployeeLogin() {
    document.getElementById('employeeLogin').style.display = 'block';
    document.getElementById('login').style.display = 'none';
  }
  
  document.getElementById('managerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const managerId = document.getElementById('managerId').value;
    const managerPassword = document.getElementById('managerPassword').value;
    
    // Send manager login details to backend
    // On successful login, show manager dashboard
    document.getElementById('managerDashboard').style.display = 'block';
    document.getElementById('managerLogin').style.display = 'none';
  });
  
  document.getElementById('employeeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const employeeId = document.getElementById('employeeId').value;
    const employeePassword = document.getElementById('employeePassword').value;
    
    // Send employee login details to backend
    // On successful login, show employee dashboard
    alert("Employee Login Successful");
  });
  
  function assignTask() {
    const employeeName = document.getElementById('employeeName').value;
    const employeeSkills = document.getElementById('employeeSkills').value;
  
    // Send task assignment data to the backend
    alert(`Task assigned to ${employeeName} with skills: ${employeeSkills}`);
  }
  