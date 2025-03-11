drop table public.application;
create table public.application
(
    application_id text
        default concat('app_', replace((uuid_generate_v4())::text, '-'::text, ''::text))
        not null
        primary key,
        name             text  not null,
        address             text not null,
        email             text not null,
        phone             text not null,
        ssn             text not null,
        total_amount_in_cents   integer not null,
        interest_rate_percent integer,
        term_months integer,
        monthly_payment_in_cents   integer,
        created_at              timestamp default now() not null,
        updated_at              timestamp default now() not null
);
