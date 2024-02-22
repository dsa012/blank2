json = {'acr': '0', 'at_hash': 'wl2iYJ4wzvOAFWJ7fdbM4w', 'aud': ['6d61ca18-1bba-4998-ac62-dbec109f356b'], 'auth_time': 1708569345, 'custom': [{'type': ['VerifiableCredential', 'Email']}, {'email': 'canav@proton.me'}, {'type': ['VerifiableCredential', 'HITCountry']}, {'country': 'Indonesia'}, {'type': ['VerifiableCredential', 'HITPicture']}, {'picture': 'https://images.unsplash.com/photo-1707699400213-847b2b852300?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}, {'type': ['VerifiableCredential', 'HITGivenName']}, {'givenName': 'Test1'}, {'type': ['VerifiableCredential', 'HITFamilyName']}, {'familyName': 'Test2'}, {'type': ['VerifiableCredential', 'HITPhoneNumber']}, {'phoneNumber': '10139332'}, {'type': ['VerifiableCredential', 'HITPostalCode']}, {'postalCode': '20119'}, {'type': ['VerifiableCredential', 'HITStreetAddress']}, {'streetAddress': 'dw'}, {'type': ['VerifiableCredential', 'HITLocality']}, {'locality': 'Amineo'}, {'did': 'did:key:zQ3shUyB3N2rFHZ4RaRSaBSb6rZq5ErdAmBLfyEprcFLQUaca'}], 'exp': 1708570251, 'iat': 1708569351, 'iss': 'https://043a1d18-9064-4353-ac82-14e04356866b.apse1.login.affinidi.io', 'jti': 'adfbe65b-c311-4969-a7bc-7d66d7de442e', 'nonce': 'fQY9fhMbjkECkGJipAAv', 'rat': 1708569322, 'sid': 'b5eb38b4-7434-490c-a646-eefe6534a764', 'sub': 'did:key:zQ3shUyB3N2rFHZ4RaRSaBSb6rZq5ErdAmBLfyEprcFLQUaca'}

print(json['custom'][1]['email'])
print(json['custom'][3]['country'])
print(json['custom'][5]['picture'])
print(json['custom'][7]['givenName'])
print(json['custom'][9]['familyName'])
print(json['custom'][11]['phoneNumber'])
print(json['custom'][13]['postalCode'])
print(json['custom'][15]['streetAddress'])
print(json['custom'][17]['locality'])
print(json['custom'][19]['birthdate'])
print(json['custom'][21]['gender'])