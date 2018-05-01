sort_okta_users.py runs in python 2.7.10

----------------------------------------

sort_okta_users.py parses the OktaPasswordHealth.csv and separates users based on the following statuses:

- active
- deprovisioned 
- locked_out 
- password_expired
- provisioned
- staged
- suspended

sort_okta_users.py then exports csvs of users grouped by status (e.g. active.csv, deprovisioned.csv, etc.) and provides a summary of each status including what percentage of total users each status grouping represents

to run, sort_okta_users.py, save sort_okta_users.py and the "OktaPasswordHealth.csv" to the same directory.

In Terminal, navigate to the directory in which you've saved both files and type "python sort_okta_users.py"
