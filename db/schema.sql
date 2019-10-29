BEGIN;
CREATE TABLE posts (
    id BIGSERIAL PRIMARY KEY,
    requestbody jsonb,
    createdat timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    remoteaddress character varying(1000),
    request_url character varying(1000)
);
COMMIT;