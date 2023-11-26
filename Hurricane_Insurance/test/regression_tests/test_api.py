import requests

BASE_URL = "https://sure-qa-challenge.vercel.app/api/quote"
STATUS_OK = 200


# Verify that POST API request for generating a quote does not require authentication
def test_generate_quote():
    payload = {
        "postalCode": "12345",
        "buildingMaterial": "straw",
        "waterProximity": "true",
    }
    response = requests.post(BASE_URL, json=payload)
    print(response.json())

    assert response.status_code == STATUS_OK
