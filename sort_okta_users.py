"""__doc__"""

# import
import csv

# define dashed line lambda for readability
DASHED_LINE = lambda: '-'

# define list of statuses and NUMBERS_OF_USERS list to be populated later
OKTA_STATUSES = [
    'ACTIVE',
    'DEPROVISIONED',
    'LOCKED_OUT',
    'PASSWORD_EXPIRED',
    'PROVISIONED',
    'STAGED',
    'SUSPENDED'
]

# define function to turn a csv into a list and store the list
def csv_to_list(okta_status):
    """ import csv and turn it into a list """
    user_list = []
    okta_status_csv = okta_status.lower() + '.csv'
    with open('OktaPasswordHealth.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = row['Login']
            user_status = row['Status']
            if user_status == okta_status:
                user_list.append([user, user_status])
                out_file = open(okta_status_csv, 'w')
            else:
                pass

    with out_file:
        writer = csv.writer(out_file)
        writer.writerow(['user', 'status'])
        writer.writerows(user_list)
        return user_list

# create a list to be populated later
NUMBERS_OF_USERS = []

# get total users
for status in OKTA_STATUSES:
    get_list = csv_to_list(status)
    number = len(get_list)
    NUMBERS_OF_USERS.append(number)
    total_users = float(sum(NUMBERS_OF_USERS))

# summary header
print "Summary"
print DASHED_LINE()

# calculate percentage of total users in each status group
for status in OKTA_STATUSES:
    get_list = csv_to_list(status)
    number = len(get_list)
    percent = number / total_users
    percent = "{:.2%}".format(percent)
    if number == 1:
        print("There is %s user (%s) in %s.csv") % (number, percent, status.lower())
    else:
        print("There are %s users (%s) in %s.csv") % (number, percent, status.lower())
