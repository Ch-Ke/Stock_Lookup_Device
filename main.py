import pandas as pd
from tabulate import tabulate
import requests
import re
import os

def main():
    while True:
        get_item_location()


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def update_spreadsheet():
    csv_download_url = ''
    csv_local_file = "test.csv"
    params = {'exportFormat': 'csv', }
    response = requests.get(csv_download_url, params=params)

    if response.status_code == 200:
        with open(csv_local_file, "wb") as file:
            file.write(response.content)
        print(f"Spreadsheet downloaded as {csv_local_file}")
    else:
        print("Download failed...")

def get_item_location():
    while True:
        user_input = input("Enter article number: ")
        article_number_pattern = r'\d\.\d{3}-\d{3}\.\d'
        if re.fullmatch(article_number_pattern, user_input):
            break
        elif len(user_input) == 8 and re.fullmatch(user_input, article_number_pattern) is None:
            user_input = f"{user_input[0]}.{user_input[1:4]}-{user_input[4:7]}.{user_input[7]}"
            break
        elif user_input == "000":
            print("updating spreadsheet...\n")
            update_spreadsheet()
        else:
            print("please enter a value in the format \"1.234-567.8\" or \"12345678\"\n")

    print("valid input, fetching item data...\n")
    spreadsheet_df = pd.read_csv('test.csv')
    result = spreadsheet_df.loc[spreadsheet_df['Article Number'] == user_input]
    print(tabulate(result, headers='keys', tablefmt='heavy_grid', showindex=False))
    input("Press enter to input another item.\n")
    cls()

if __name__ == "__main__":
    main()
