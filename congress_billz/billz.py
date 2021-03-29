import os
import datetime
import requests


api_key = os.environ.get('api_key')
# get from api?
valid_collections = ['USCOURTS', 'BILLS', 'CHRG', 'FR', 'GAOREPORTS', 'GOVPUB', 'CPD', 'CZIC', 'CFR', 'PLAW', 'CREC',
                     'CCAL', 'GPO', 'CDOC', 'CRECB', 'CPRT', 'PAI', 'USCODE', 'ERIC', 'BUDGET', 'ECONI', 'LSA', 'PPP',
                     'STATUTE', 'HOB', 'ERP', 'GOVMAN', 'CDIR', 'HMAN', 'HJOURNAL', 'SMAN']


def get_date(date_type):
    date = input(f'Enter {date_type} date in YYYY-MM-DD format: ')
    validate_date(date)
    return date


def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(f'{date} invalid please enter date in YYYY-MM-DD format.')
        get_date()


# case insensitive
def get_collection():
    user_collection = input('Enter collection: ')
    if validate_collection(user_collection):
        return user_collection


def validate_collection(user_collection):
    if user_collection in valid_collections:
        return True
    else:
        print(f'{user_collection} not valid, please choose a valid collection.')
        get_collection()


collection = get_collection()
start_date = get_date('start')
end_date = get_date('end')
url = f'https://api.govinfo.gov/published/{start_date}/{end_date}?offset=0&pageSize=10&collection={collection}&api_key={api_key} '
billz = requests.get(url)
print(billz.text)
