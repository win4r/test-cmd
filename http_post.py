import requests


def get_request(url: str, params: dict = None, headers: dict = None) -> requests.Response:
    """
    Make an HTTP GET request.

    Args:
        url: The URL to send the request to
        params: Query parameters to include in the URL
        headers: Optional headers to include

    Returns:
        Response object
    """
    response = requests.get(url, params=params, headers=headers)
    return response


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


def delete_request(url: str, params: dict = None, json_data: dict = None, headers: dict = None) -> requests.Response:
    """
    Make an HTTP DELETE request.

    Args:
        url: The URL to send the request to
        params: Query parameters to include in the URL
        json_data: JSON data to send in the request body (optional)
        headers: Optional headers to include

    Returns:
        Response object
    """
    response = requests.delete(url, params=params, json=json_data, headers=headers)
    return response


def put_request(url: str, data: dict = None, json_data: dict = None, headers: dict = None) -> requests.Response:
    """
    Make an HTTP PUT request.

    Args:
        url: The URL to send the request to
        data: Form data to send (application/x-www-form-urlencoded)
        json_data: JSON data to send (application/json)
        headers: Optional headers to include

    Returns:
        Response object
    """
    response = requests.put(url, data=data, json=json_data, headers=headers)
    return response


if __name__ == "__main__":
    # Example usage - GET request
    get_url = "https://httpbin.org/get"
    params = {"name": "John", "age": 30}
    response = get_request(get_url, params=params)
    print("GET Request:")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    print()

    # Example usage - POST request
    post_url = "https://httpbin.org/post"
    payload = {"name": "John", "age": 30}
    response = post_request(post_url, json_data=payload)
    print("POST Request:")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    print()

    # Example usage - PUT request
    put_url = "https://httpbin.org/put"
    payload = {"name": "John Updated", "age": 31}
    response = put_request(put_url, json_data=payload)
    print("PUT Request:")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    print()

    # Example usage - DELETE request
    delete_url = "https://httpbin.org/delete"
    response = delete_request(delete_url, params={"id": 123})
    print("DELETE Request:")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
