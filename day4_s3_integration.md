What I Built:
The Vault: Created an S3 bucket named yusuf-babystore-data-2026 to hold company data.

The Bridge: Installed the boto3 library so Python can talk to AWS services.

The Permissions: Attached the S3-Reviewer IAM Role to my EC2 server. This is the "Least Privilege" way to give access without using passwords.

The Result:
I successfully ran a Python script that pulled a text file from the secure S3 bucket and displayed it in the terminal.
