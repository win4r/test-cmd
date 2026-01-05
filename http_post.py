import requests


def post_request(url: str, data: dict = None, json_data: dict = None, headers: dict = None) -> requests.Response:
    """
    Make an HTTP POST request.

    Args:
        url: The URL to send the request to
        data: Form data to send (application/x-www-form-urlencoded)
        json_data: JSON data to send (application/json)
        headers: Optional headers to include

    Returns:
        Response object
    """
    response = requests.post(url, data=data, json=json_data, headers=headers)
    return response


if __name__ == "__main__":
    # Example usage
    url = "https://httpbin.org/post"

    # JSON POST request
    payload = {"name": "John", "age": 30}
    response = post_request(url, json_data=payload)

    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
