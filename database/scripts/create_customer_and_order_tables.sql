drop table public.order;
drop table public.customer;

create table public.customer
(
    customer_id text
        default concat('customer_', replace((uuid_generate_v4())::text, '-'::text, ''::text))
        not null
        primary key,
    name        text not null,
    email       text not null,
    note        text,
    created_at  timestamp default now() not null,
    updated_at  timestamp default now() not null
);

create table public.order
(
    order_id text
        default concat('order_', replace((uuid_generate_v4())::text, '-'::text, ''::text))
        not null
        primary key,
    customer_id text references customer(customer_id),
    total_amount_in_cents   integer not null,
    description             text,
    created_at              timestamp default now() not null,
    updated_at              timestamp default now() not null
);

