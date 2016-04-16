import vdp_utils
import json


BASE_URL = 'https://sandbox.api.visa.com'


def pullFunds(S):
    uri = '/visadirect/fundstransfer/v1/pullfundstransactions/'
    body = json.loads('''{
        "acquirerCountryCode": "840",
        "acquiringBin": "408999",
        "amount": "124.02",
        "businessApplicationId": "AA",
        "cardAcceptor": {
            "address": {
                "country": "USA",
                "county": "San Mateo",
                "state": "CA",
                "zipCode": "94404"
            },
            "idCode": "ABCD1234ABCD123",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "ABCD1234"
        },
        "cavv": "0700100038238906000013405823891061668252",
        "foreignExchangeFeeTransaction": "11.99",
        "localTransactionDateTime": "2016-04-16T14:44:04",
        "retrievalReferenceNumber": "330000550000",
        "senderCardExpiryDate": "2015-10",
        "senderCurrencyCode": "USD",
        "senderPrimaryAccountNumber": "4895142232120006",
        "surcharge": "11.99",
        "systemsTraceAuditNumber": "451001"
    }''')
    r = S.post(BASE_URL + uri, json=body)
    return r


def main():
    user_id = 'put your user id for the app from VDP Portal here'
    password = 'put your password for the app from VDP Portal here'
    cert = 'put the client certificate pem file path here'
    key = 'put the private key pem file path here'

    with vdp_utils.MSession(user_id, password, cert, key) as S:
        S.headers.update({'content-type': 'application/json',
                         'accept': 'application/json'})
        r = pullFunds(S)

    print r.status_code
    print r.content


if __name__ == '__main__':
    main()
