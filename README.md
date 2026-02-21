Day 6 GitHub Report: Identity-Based Security
Objective
Transition the Babystore Analytics engine from using static AWS Access Keys to a hardened, identity-based authentication model.

Key Achievements

IAM Role Implementation: Created and attached an IAM Role (EC2-S3-ReadOnly-Role) with AmazonS3ReadOnlyAccess policy to the EC2 instance.

Credential Elimination: Successfully ran the data pipeline without aws configure or storing secret keys on the server's disk.

Security Group Hardening: Configured specific inbound rules for Port 22 (Management) and Port 5000 (Application) while maintaining a "Least Privilege" network posture.

Infrastructure Recovery: Rebuilt the application environment from scratch on a new Amazon Linux 2023 instance to verify the portability of the code and security configuration.
