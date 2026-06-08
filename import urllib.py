import requests
from bs4 import BeautifulSoup


def print_secret_message(url):
    """
    Fetches data from a published Google Doc, parses a table of 
    coordinates and characters, and prints a grid to reveal a message.
    """
    try:
        # 1. Fetch the content of the Google Doc
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # 2. Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Google Docs published as web pages put data in a <table> element
        table = soup.find('table')
        if not table:
            print("Could not find a table in the provided URL.")
            return

        # 3. Extract data from the table rows
        # We skip the first row as it contains the headers (x-coordinate, Character, y-coordinate)
        rows = table.find_all('tr')
        data_points = []

        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) >= 3:
                try:
                    # Extract text and clean it
                    x = int(cols[0].get_text().strip())
                    char = cols[1].get_text().strip()
                    y = int(cols[2].get_text().strip())
                    data_points.append((x, y, char))
                except ValueError:
                    # Skip rows where coordinates aren't valid integers
                    continue

        if not data_points:
            print("No valid data points found in the table.")
            return

        # 4. Determine the dimensions of the grid
        # The grid size is determined by the maximum x and y coordinates found
        max_x = max(point[0] for point in data_points)
        max_y = max(point[1] for point in data_points)

        # 5. Create a coordinate map for easy lookup
        # Using a dictionary where key is (x, y) and value is the character
        grid_map = {(x, y): char for x, y, char in data_points}

        # 6. Print the grid
        # Note: y=0 is the bottom, so we iterate from max_y down to 0
        for y in range(max_y, -1, -1):
            row_string = ""
            for x in range(max_x + 1):
                # Use the character if it exists at this coordinate, otherwise use a space
                row_string += grid_map.get((x, y), ' ')
            print(row_string)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the document: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_secret_message(url)
