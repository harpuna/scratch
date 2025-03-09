import os
from pathlib import Path

import pytest

from app import create_app
from config import app_config
from models import Order


@pytest.fixture(scope="module")
def app():
    # The app expects to be in the root folder
    current_dir = os.getcwd()
    os.chdir(Path(__file__).parents[2])
    app_ = create_app(app_config)
    os.chdir(current_dir)
    return app_






@pytest.fixture
def mock_db_order(mocker):
    order_mock = mocker.patch(
        "routes.order.Order.select"
    )
    order = Order(
        id="order_2",
        customer_id="customer_3",
        description="test order",
        total_amount_in_cents=1488
    )
    order_mock.return_value = order

    # PartnerCredentials(
    #     uuid="test-partner-cred-uuid",
    #     credential_uuid="test-cred-uuid",
    #     partner_uuid="test-partner-uuid",
    #     company_name="test-company-name",
    #     contact_email="test-contact-email",
    #     contact_phone="test-contact-phone",
    # )

    return order_mock

@pytest.fixture
def mock_db_all_orders(mocker):
    order_mock = mocker.patch(
        "routes.order.Order.all"
    )
    order = Order(
        id="order_1",
        customer_id="customer_2",
        description="test order",
        total_amount_in_cents=1995
    )
    order_mock.return_value = [order,order]

    # PartnerCredentials(
    #     uuid="test-partner-cred-uuid",
    #     credential_uuid="test-cred-uuid",
    #     partner_uuid="test-partner-uuid",
    #     company_name="test-company-name",
    #     contact_email="test-contact-email",
    #     contact_phone="test-contact-phone",
    # )

    return order_mock

# @pytest.fixture
# def member_body():
#     return {
#         "birthday": "2020-12-08",
#         "created_at": "2020-12-08",
#         "credit_scores": [],
#         "email": "email",
#         "email_consent": True,
#         "first_name": "first_name",
#         "last_name": "last_name",
#         "member_addresses": [],
#         "member_id": "member_id",
#         "auth0_user_id": "auth0_user_id",
#         "phone_number": "phone_number",
#         "ssn_consent": True,
#         "employer": "employer",
#         "monthly_income_dollars": 5000,
#     }
#
#
# @pytest.fixture
# def application_body():
#     return {
#         "application_id": "app-id",
#         "building_id": "jetty_building_id",
#         "created_at": "2021-06-30T09:07:14.061261-05:00",
#         "document_ids": None,
#         "enrollment_end_date": "2022-06-30",
#         "enrollment_start_date": "2021-08-01",
#         "expiration_date": "2021-07-30",
#         "loan_id": "JIL-2021-06303219CE",
#         "member_id": "member_id",
#         "state": "submitted",
#         "updated_at": None,
#     }
#
#
# @pytest.fixture()
# def full_application_body(application_body):
#     return {
#         "application": application_body,
#         "loan_details": {},
#         "application_data": {
#             "monthly_rentable_items_amount_cents": 0,
#             "lease_start_date": "2021-07-01",
#             "borrowers_last_name": "string",
#             "origination_fee": 0,
#             "credit_score": "string",
#             "application_state": "incomplete",
#             "monthly_income_cents": 0,
#             "monthly_rentable_items": "string",
#             "tags": "string",
#             "address": "string",
#             "created_at": "2021-07-01T15:55:54.579Z",
#             "application_data_id": "string",
#             "payment_dates": "string",
#             "monthly_variable_rent_buffer_amount_cents": 0,
#             "employer": "string",
#             "lease_type": "new",
#             "monthly_rent_cents": 0,
#             "monthly_loan_amount_cents": 0,
#             "monthly_fee_cents": 0,
#             "borrowers_first_name": "string",
#             "lease_end_date": "2021-07-01",
#             "scp_date": "2021-07-01",
#             "coverage_cents": 0,
#             "stipulations": "string",
#             "installments_cents": "string",
#             "servicing_fee": 0,
#         },
#     }


# @pytest.fixture(autouse=True)
# def os_environ_mock(mocker):
#     mocker.patch.dict(
#         "os.environ",
#         {
#             "env": "env_string",
#         },
#     )
