from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = [{'id': emp.id, 'name': emp.name, 'age': emp.age, 'address': emp.address,
                 'salary': emp.salary, 'designation': emp.designation, 'mobile_number': emp.mobile_number} for emp in employees]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.create(name=data['name'], age=data['age'], address=data['address'],
                                           salary=data['salary'], designation=data['designation'], mobile_number=data['mobile_number'])
        return JsonResponse({'id': employee.id, 'message': 'Employee created successfully'}, status=201)

@csrf_exempt
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee does not exist'}, status=404)

    if request.method == 'GET':
        data = {'id': employee.id, 'name': employee.name, 'age': employee.age, 'address': employee.address,
                'salary': employee.salary, 'designation': employee.designation, 'mobile_number': employee.mobile_number}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        employee.name = data.get('name', employee.name)
        employee.age = data.get('age', employee.age)
        employee.address = data.get('address', employee.address)
        employee.salary = data.get('salary', employee.salary)
        employee.designation = data.get('designation', employee.designation)
        employee.mobile_number = data.get('mobile_number', employee.mobile_number)
        employee.save()
        return JsonResponse({'message': 'Employee updated successfully'})

    elif request.method == 'DELETE':
        employee.delete()
        return JsonResponse({'message': 'Employee deleted successfully'}, status=204)

"""
To check working of API in POSTMAN:
Sure, here's how you can test each API endpoint using Postman:

GET /employees: Retrieve all employees
Open Postman and create a new request.
Set the request type to GET.
Enter the URL of your Django server followed by the /employees endpoint (e.g., http://localhost:8000/employees/).
Send the request.
You should receive a JSON response containing a list of all employees.

POST /employees: Create a new employee
Create another new request in Postman.
Set the request type to POST.
Enter the URL of your Django server followed by the /employees endpoint (e.g., http://localhost:8000/employees/).
In the request body, select "raw" and choose JSON format.
Enter the employee data in JSON format (e.g., {"name": "John Doe", "age": 30, ...}).
Send the request.
You should receive a JSON response confirming that the employee was created successfully.

GET /employees/<id>: Retrieve details of a specific employee
Create a new request in Postman.
Set the request type to GET.
Enter the URL of your Django server followed by the /employees/<id> endpoint, replacing <id> with the actual ID of the employee you want to retrieve (e.g., http://localhost:8000/employees/1 to retrieve details of the employee with ID 1).
Send the request.
You should receive a JSON response containing the details of the specified employee.

PUT /employees/<id>: Update details of a specific employee
Create a new request in Postman.
Set the request type to PUT.
Enter the URL of your Django server followed by the /employees/<id> endpoint, replacing <id> with the actual ID of the employee you want to update (e.g., http://localhost:8000/employees/1 to update details of the employee with ID 1).
In the request body, select "raw" and choose JSON format.
Enter the updated employee data in JSON format (e.g., {"name": "Updated Name", "age": 35, ...}).
Send the request.
You should receive a JSON response confirming that the employee was updated successfully.

DELETE /employees/<id>: Delete a specific employee
Create a new request in Postman.
Set the request type to DELETE.
Enter the URL of your Django server followed by the /employees/<id> endpoint, replacing <id> with the actual ID of the employee you want to delete (e.g., http://localhost:8000/employees/1 to delete the employee with ID 1).
Send the request.
You should receive a JSON response confirming that the employee was deleted successfully.

To POST Data JSON Data should be in below form:
{
    "id":6,
    "name": "Foram Umang",
    "age": 32,
    "address": "Bangalore",
    "salary": 10000000,
    "designation": "Project Manager",
    "mobile_number": "9650764987"
}
"""