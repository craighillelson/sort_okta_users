""" __doc__ """

import csv
import re
from collections import namedtuple

RTN = lambda: "\n"

OKTA_STATUSES = [
    "ACTIVE",
    "DEPROVISIONED",
    "LOCKED_OUT",
    "PASSWORD_EXPIRED",
    "PROVISIONED",
    "STAGED",
    "SUSPENDED",
    ]

ALL_USERS_DCT = {}
ACTIVE_DCT = {}
DEPROVISIONED_DCT = {}
INACTIVE_DCT = {}
LOCKED_OUT_DCT = {}
PASSWORD_EXPIRED_DCT = {}
PROVISIONED_DCT = {}
STAGED_DCT = {}
SUSPENDED_DCT = {}

HEADERS = [
    'user',
    'status',
    ]

# define functions
def add_to_dct(dct):
    """ add to dictionary """
    dct[row.Login] = row.Status


def print_dct(user_status, dct):
    """ calculate % of users per status, print users """
    if dct:
        percentage = "{0:.2%}".format(len(dct) / len(ALL_USERS_DCT))
        print(f"Satus: {user_status}\nUsers: {len(dct)}. {percentage}\n")
        for user, status in dct.items():
            print(user, status)
        print(RTN())


def write_to_csv(name_of_file, status_dct):
    """ write dictionary to csv """
    if status_dct:
        with open(name_of_file, 'w') as out_file:
            out_csv = csv.writer(out_file)
            out_csv.writerow(HEADERS)
            for user, status in status_dct.items():
                user_stats = (user, status)
                out_csv.writerow(user_stats)


# open csv, populate dictionaries based on user status
with open("OktaPasswordHealth.csv") as in_file:
    F_CSV = csv.reader(in_file)
    HEADINGS = [re.sub('[^a-zA-Z]', '_', h) for h in next(F_CSV)]
    ROW = namedtuple('Row', HEADINGS)
    for r in F_CSV:
        row = ROW(*r)
        ALL_USERS_DCT[row.Login] = row.Status
        okta_user_status = row.Status
        if row.Status == "ACTIVE":
            add_to_dct(ACTIVE_DCT)
        elif row.Status == "DEPROVISIONED":
            add_to_dct(DEPROVISIONED_DCT)
        elif row.Status == "LOCKED_OUT":
            add_to_dct(LOCKED_OUT_DCT)
        elif row.Status == "PASSWORD_EXPIRED":
            add_to_dct(PASSWORD_EXPIRED_DCT)
        elif row.Status == "PROVISIONED":
            add_to_dct(PROVISIONED_DCT)
        elif row.Status == "STAGED":
            add_to_dct(STAGED_DCT)
        else:
            add_to_dct(SUSPENDED_DCT)


# display results
print(RTN())
print(f"Total users: {len(ALL_USERS_DCT)}\n")
print_dct("ACTIVE", ACTIVE_DCT)
print_dct("DEPROVISIONED", DEPROVISIONED_DCT)
print_dct("LOCKED OUT", LOCKED_OUT_DCT)
print_dct("PASSWORD EXPIRED", PASSWORD_EXPIRED_DCT)
print_dct("STAGED", STAGED_DCT)
print_dct("SUSPENDED", SUSPENDED_DCT)

# write to csvs
write_to_csv("active_users.csv", ACTIVE_DCT)
write_to_csv("deprovisioned_users.csv", DEPROVISIONED_DCT)
write_to_csv("locked_out_users.csv", LOCKED_OUT_DCT)
write_to_csv("password_expired_users.csv", PASSWORD_EXPIRED_DCT)
write_to_csv("staged_users.csv", STAGED_DCT)
write_to_csv("suspended_users.csv", SUSPENDED_DCT)
