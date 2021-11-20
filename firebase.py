from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import auth
from rest_framework.response import Response
import firebase_admin
cred = credentials.Certificate('tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
# 'databaseURL': 'https://fitness-6e690.firebaseio.com'
firebase_admin.initialize_app(cred, {'databaseURL': 'https://tech-event-nov-21-default-rtdb.firebaseio.com/'})
"""sap_id = "500067935"
ref = db.reference('/acm_acmw_members/{}'.format(sap_id)).get()
print(ref)
"""
"""try:
    #auth.set_custom_user_claims(
    #    "wn4k8LGHDUfchOnqg85DhkK9I4U2", {'payment': True})          # temporary...  will be set to False
    #user = auth.get_user("wn4k8LGHDUfchOnqg85DhkK9I4U2")
    sap_id = "10001"
    user = auth.create_user(display_name=sap_id)
    print(user.uid)

except firebase_admin.exceptions.FirebaseError as ex:
    print(f'{ex}')
"""
"""ref_fee = db.reference('membership_fee_2020/')
refer = ref_fee.get()

membership_type = "International"
amount = refer.get("{}".format(membership_type))

print(amount)"""

"""
sap_id = "400077185"
ref_member = db.reference('acm_acmw_members/').order_by_child('sap').equal_to(sap_id).get()

if(ref_member):
    print("true")
else:
    print("false")
#refer_member = ref_member.get()
print(ref_member)


"""

# user = auth.update_user(
#     "WI88aMyzHEcyra1HSmf8gcFA1wM2",
#     email='500084175@stu.upes.ac.in',
#     #phone_number='+15555550100',
#     #email_verified=True,
#     password='500084175',
#     display_name='500084175',
#     #photo_url='http://www.example.com/12345678/photo.png',
#     #disabled=False
#     )
# print(user._data)
#user = auth.get_user("TDcwJGB5WOeS0zCcafUz5R3vZyP2")
#print(user._data)

"""
accounts = [
    500055555,
    500076578,
    500085014,
    500083269,
    500083287,
    500085965,
    500084672,
    500084901,
    500082883,
    500085061,
    500084937,
    500082578,
    500083382,
    500085033,
    500086929,
    500083487,
    500077097,
    500082908,
    500083218,
    500085093,
    500086354,
    500084611,
    500076593,
    500083359,
    500075119,
    500084671,
    500083538,
    500084888,
    500086020,
    500084110,
    500086396,
    500085035,
    500067782,
    500083466,
    500075359,
    500082378,
    500082963,
    500067626,
    500069950,
    500082431,
    500086686,
    500068743,
    500077736,
    500086295,
    500086296,
    500087021,
    500085570,
    500085833,
    500075338,
    500083149,
    500086397,
    500080975,
    500081292,
    500083102,
    500084970,
    500083065,
    500082715,
    500085015,
    500084883,
    500084175,
    500082607,
    500082343,
    500084995,
    500075886,
    500083174,
    500083325,
    500082789,
    500083599,
    500085084,
    500076104,
    500083038,
    500083403,
    500083141,
    500061018,
    500075342,
    500085046,
    500082573,
    500082727,
    500067266,
    500086213,
    500099999,
]
"""
#print(len(accounts))
"""
for i in range(len(accounts)):
    sap = str(accounts[i])
    email = str(sap+'@stu.upes.ac.in')
    name = str(sap)
    password = str(sap)

    #print(email, name, password)

    user = auth.create_user(
    email = email,
    email_verified = False,
    password = sap,
    display_name = sap,
    disabled = False,
    )

    print(user._data)
"""

user = auth.create_user(
    email = '500011111@stu.upes.ac.in',
    #phone_number = '+15555550102',
    email_verified = False,
    password = '500011111',
    display_name = 'Test1',
    disabled = False,
)

print(user._data)