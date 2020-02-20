BEGIN;
CREATE TABLE posts (
    id BIGSERIAL PRIMARY KEY,
    request_body jsonb,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    remote_address character varying(1000),
    request_url character varying(1000)
);
COMMIT;