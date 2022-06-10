import pygsheets as pygsheets
import pandas as pd


def write2GoogleSheet():
    # goole_file_name
    goole_file_name = "testGoogleSheet"

    # authorization
    gc = pygsheets.authorize(service_file='service_account.json')

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = ['John', 'Steve', 'Sarah', 'Apple', 'Orange']
    df['age'] = ['20', '30', '34', '33', '12']
    df['Engish_Score'] = ['20', '30', '34', '33', '12']
    df['Computer_Score'] = ['20', '30', '34', '33', '12']

    # open the google spreadsheet
    sh = gc.open(goole_file_name)

    # select the first sheet
    wks = sh[0]

    # update the first sheet with df, starting at cell B2.
    wks.set_dataframe(df, (1, 1))


def readGoogleSheet():

    goole_file_name = "testGoogleSheet"

    # authorization
    gc = pygsheets.authorize(service_file='service_account.json')

    # open the google spreadsheet
    sh = gc.open(goole_file_name)

    worksheet = sh[0]  # -> 0 - first sheet, 1 - second sheet etc.

    # Create empty dataframe
    data = pd.DataFrame(worksheet)
    print(data)
    return data


if __name__ == '__main__':
    write2GoogleSheet()
    readGoogleSheet()
