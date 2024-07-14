from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ResponseStatu(BaseModel):
    status_code: int
    status: str


class ListInfo(BaseModel):
    has_more_rows: bool
    start_index: int
    sort_field: str
    total_count: int
    page: int
    sort_order: str
    get_total_count: str
    row_count: int


class ServiceCategory(BaseModel):
    id: str


class Template(BaseModel):
    is_service_template: bool
    service_category: ServiceCategory
    name: str
    id: str


class Serviceplan(BaseModel):
    id: str


class AccountcontractItem(BaseModel):
    serviceplan: Serviceplan
    isactivecontract: bool
    contractnumber: str
    roundoffvalue: str
    name: str
    contractname: str
    description: str
    currency: str
    billunclosed: bool
    id: str


class Group(BaseModel):
    name: str
    id: str


class ProfilePic(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account(BaseModel):
    name: str
    id: str


class Requester(BaseModel):
    email_id: Optional[str]
    phone: Any
    name: str
    mobile: Any
    profile_pic: ProfilePic
    org_user_status: str
    id: str
    account: Optional[Account] = None
    is_vipuser: Optional[bool] = None


class CreatedTime(BaseModel):
    display_value: str
    value: str


class ProductType(BaseModel):
    id: str


class ProductItem(BaseModel):
    part_no: str
    product_type: ProductType
    inactive: bool
    warranty_period_years: str
    name: str
    comment: Optional[str]
    id: str
    warranty_period_months: str


class ProfilePic1(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account1(BaseModel):
    name: str
    id: str


class TechnicianItem(BaseModel):
    email_id: str
    phone: Optional[str]
    name: str
    mobile: Optional[str]
    profile_pic: ProfilePic1
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Account1


class PriorityItem(BaseModel):
    color: str
    name: str
    id: str


class ProfilePic2(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account2(BaseModel):
    name: str
    id: str


class CreatedBy(BaseModel):
    email_id: Optional[str]
    phone: Optional[str]
    name: str
    mobile: Optional[str]
    profile_pic: ProfilePic2
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Optional[Account2] = None


class DueByTimeItem(BaseModel):
    display_value: str
    value: str


class CountryItem(BaseModel):
    id: str


class TimezoneItem(BaseModel):
    id: str


class AccountItem(BaseModel):
    country: Optional[CountryItem]
    inactive: bool
    timezone: Optional[TimezoneItem]
    name: str
    industry: Any
    id: str
    ciid: str


class Status(BaseModel):
    color: Optional[str]
    name: str
    id: str


class Request(BaseModel):
    template: Template
    short_description: str
    subject: str
    time_elapsed: Optional[Any] = None
    is_service_request: bool
    accountcontract: Optional[AccountcontractItem]
    cancel_requested: bool
    id: str
    group: Group
    requester: Requester
    created_time: CreatedTime
    product: Optional[ProductItem]
    subaccount: Any
    is_overdue: bool
    technician: Optional[TechnicianItem]
    is_billable: bool
    priority: Optional[PriorityItem]
    created_by: CreatedBy
    due_by_time: Optional[DueByTimeItem]
    response_time_elapsed: Any
    site: Any
    cancel_requested_is_pending: bool
    account: Optional[AccountItem]
    status: Status

    def representation(self):
        return {
                "id": self.id,
                "subject": self.subject,
                }

    def delete(self):
        pass


class Model(BaseModel):
    response_status: List[ResponseStatu]
    list_info: ListInfo
    requests: List[Request]

