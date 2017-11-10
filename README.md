# optrak
-
This program represents a proof of concept of a web application that would allow
healthcare providers to securely exchange patient opioid prescription information.


Installation Instruction:

1. Ensure Django is installed on your local machine.
2. Install pip if you need to update any python libraries.
3. Clone the repository


Database Setup:

1. Download and Install Postgresql
  - brew install postgres
  - brew services start postgres
2. Open a postgres command line tool
  - psql postgres
3. Create a new database called Optrak
  - CREATE DATABASE optrak;
4. Create a new user doctor with password Optrak
  - CREATE ROLE doctor WITH LOGIN PASSWORD 'optrak';
5. Grant user all privleges on the table
  - GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO doctor;
