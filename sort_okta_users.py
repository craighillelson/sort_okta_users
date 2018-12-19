# import
import csv

# define function
def dashed_line():
    print '-' * 40

# define list of statuses and numbers_of_users list to be populated later
okta_statuses = [
    'ACTIVE',
    'DEPROVISIONED',
    'LOCKED_OUT',
    'PASSWORD_EXPIRED',
    'PROVISIONED',
    'STAGED', 
    'SUSPENDED'
]

numbers_of_users = []

# define function to turn a csv into a list and store the list
def csv_to_list(okta_status):
    user_list = []
    okta_status_csv = okta_status.lower() + '.csv'
    with open('OktaPasswordHealth.csv') as csvfile:  
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = row['Login']
            status = row['Status']
            if status == okta_status:
                user_list.append([user, status])
                out_file = open(okta_status_csv, 'w')
            else:
                pass

    with out_file:
        writer = csv.writer(out_file)
        writer.writerow(['user', 'status'])
        writer.writerows(user_list)
        return user_list

# create a list to be populated later
numbers_of_users = []

# get total users
for status in okta_statuses:
    get_list = csv_to_list(status)
    number = len(get_list)
    numbers_of_users.append(number)
    total_users = float(sum(numbers_of_users))

# summary header
print "Summary"
dashed_line()

# calculate percentage of total users in each status group
for status in okta_statuses:
    get_list = csv_to_list(status)
    number = len(get_list)
    percent = number / total_users
    percent = "{:.2%}".format(percent)
    if number == 1:
        print("There is %s user (%s) in %s.csv") % (number, percent, status.lower())
    else:
        print("There are %s users (%s) in %s.csv") % (number, percent, status.lower())