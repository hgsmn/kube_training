import requests

def check_csp_header(url):
    try:
        # Make a GET request to the provided URL
        response = requests.get(url)

        # Check if the CSP header exists in the response headers
        csp_header = response.headers.get("Content-Security-Policy")

        if csp_header:
            print("CSP header found:")
            print(csp_header)
        else:
            print("CSP header is missing.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the URL you want to check
    url_to_check = "http://localhost:8100/"
    check_csp_header(url_to_check)
