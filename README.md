# Overview

Python 3.8 script to separate Okta users based on the following statuses:

- ACTIVE
- DEPROVISIONED 
- LOCKED_OUT 
- PASSWORD_EXPIRED
- PROVISIONED
- STAGED
- SUSPENDED

Following separating users into dictionaries, "sort_okta_users_by_status.py" exports csvs of users grouped by status (e.g. active_users.csv, deprovisioned_users.csv, etc.) and calculartes what percentage of total users each status grouping represents.

To run, save "sort_okta_users_by_status.py" and the "OktaPasswordHealth.csv" to the same directory.

In Terminal, navigate to the directory in which you've saved both files and type "python3.8 sort_okta_users_by_status.py"
