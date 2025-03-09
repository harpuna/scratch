this is an unmerged README on develop branch

### Overview



### Setup

1. Python 
   2. is installed?
      2. `which python` or `which python3`
      3. `python -V` or `python3 -V`
      4. Tip: nice alias to add: 
         5. `alias python="python"`
   4. No? Ex for OSX:
      5. https://www.python.org/downloads/macos/
      6. `which python3`
      7. .bashrc or .profile: `export PATH=/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH` (or whatever the result of which command)
      8. .bashrc or .profile: `export PYTHONPATH=./`
2. Node
   3. Is installed?
      4. `node --version`
   5. No?
      6. `nvm install --lts`
      7. `npm --version`
      8. `node --version`
9. Postgres
   10. Easy install https://postgresapp.com/
   11. Create the db
       12. `CREATE DATABASE flask_db;`
       13. `CREATE USER flask_user WITH PASSWORD 'flask_password';`
       15. `ALTER DATABASE flask_db OWNER to flask_user;`
       14. `GRANT ALL PRIVILEGES ON DATABASE flask_db TO flask_user;`
       16. `GRANT ALL ON ALL TABLES TO flask_user;`
   17. Test the connection 
18. Github
    3. Create ssh keys to authenticate with github.  Ex:
       2. `ssh-keygen -t ed25519 -C "you@email.com"`
       3. `eval "$(ssh-agent -s)"`
       4. `ssh-add ~/.ssh/id_ed2551911`
    5. Clone this repo 
       6. `git clone git@github.com:harpuna/scratch.git`

      
### Build

1. Install requirements
   2. `pip install -r requirements.txt`
1. create the tables
   2. `PGPASSWORD=flask_password psql -U flask_user -d flask_db -a -f create_customer_and_order_tables.sql`
   2. 

### Start Servers

1. Start and verify Flask server:
   2. `bin/run.sh`
   2. `curl --location 'http://127.0.0.1:5000/health'`
   3. Browser: http://127.0.0.1:5000/web/
4. Start the React server
   5. `cd test-react-app`
   2. `npm run dev`
   3. Browser: http://localhost:5173/

    
### Maintenance

1. Adding a new lib, ex:
   2. `pip install flask flask-sqlalchemy psycopg2-binary`
   3. `pip freeze > requirements.txt`
   4. `pip install -r requirements.txt`
