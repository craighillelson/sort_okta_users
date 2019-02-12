# Overview

Python 3.7.2 script to separate Okta users based on the following statuses:

- active
- deprovisioned 
- locked_out 
- password_expired
- provisioned
- staged
- suspended

sort_okta_users_by_status.py then exports csvs of users grouped by status (e.g. active_users.csv, deprovisioned_users.csv, etc.) and provides a summary of each status including what percentage of total users each status grouping represents.

To run, save "sort_okta_users_by_status.py" and the "OktaPasswordHealth.csv" to the same directory.

In Terminal, navigate to the directory in which you've saved both files and type "python3 sort_okta_users_by_status.py"
