import requests

def test_add_numbers():
    num1 = 10
    num2 = 20
    expected_result = 30
    response = requests.get(f"http://devopspythonapp.westus.azurecontainer.io:5000/add?num1={num1}&num2={num2}")
    assert response.status_code == 200
    assert response.text.strip() == str(expected_result)