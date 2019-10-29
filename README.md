# HTTP Request Tester
A simple flask app used primarily to debug webhooks for services that you don't have control over.

# Running locally
## with docker:
run `docker-compose up`
run the contents of `db/schema.sql` on your db to build the database schema

## without docker:
first ensure your environment variables are set up according to the `.sample.env` file
run the contents of `db/schema.sql` on your db to build the database schema
then:
`virtualenv env`
`source env/bin/activate`
`pip install -r requirements.txt`
`python app.py`

# Usage
Register `/request` as a webhook to the service you're testing
Query the database for incoming requests to inspect the request body