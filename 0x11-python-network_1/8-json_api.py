#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

def main():
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
                
    payload = {"q": letter}
    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        response_json = response.json()

        if not response_json:
            print("No result")
        else:
            print(f"[{response_json['id']}] {response_json['name']}")
                                                                                                                                                                
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()

