from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ResponseStatu(BaseModel):
    status_code: int
    status: str


class ListInfo(BaseModel):
    has_more_rows: bool
    start_index: int
    page: int
    start_count: int
    row_count: int


class Request(BaseModel):
    subject: str
    id: str


class TypeItem(BaseModel):
    color: str
    name: str
    id: str


class ActualEndTimeItem(BaseModel):
    display_value: str
    value: str


class ActualStartTimeItem(BaseModel):
    display_value: str
    value: str


class GroupItem(BaseModel):
    name: str
    id: str


class ProfilePic(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account(BaseModel):
    name: str
    id: str


class OwnerItem(BaseModel):
    email_id: str
    phone: Optional[str]
    name: str
    mobile: Any
    profile_pic: ProfilePic
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Account


class CreatedTime(BaseModel):
    display_value: str
    value: str


class PriorityItem(BaseModel):
    color: str
    name: str
    id: str


class ProfilePic1(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account1(BaseModel):
    name: str
    id: str


class CreatedBy(BaseModel):
    email_id: Optional[str]
    phone: Optional[str]
    name: str
    mobile: Optional[str]
    profile_pic: ProfilePic1
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Optional[Account1] = None


class DueByTimeItem(BaseModel):
    display_value: str
    value: str


class DaysDiff(BaseModel):
    diff_key: str
    diff: str


class ScheduledEndTimeItem(BaseModel):
    display_value: str
    days_diff: DaysDiff
    value: str


class EstimatedEffort(BaseModel):
    display_value: str
    hours: str
    minutes: str
    days: str


class CountryItem(BaseModel):
    id: str


class TimezoneItem(BaseModel):
    id: str


class IndustryItem(BaseModel):
    id: str


class AccountItem(BaseModel):
    country: Optional[CountryItem]
    inactive: bool
    timezone: Optional[TimezoneItem]
    name: str
    industry: Optional[IndustryItem]
    id: str
    ciid: str


class ScheduledStartTimeItem(BaseModel):
    display_value: str
    value: str


class Status(BaseModel):
    color: str
    name: str
    id: str


class Task(BaseModel):
    template: Any
    request: Optional[Request] = None
    percentage_completion: int
    email_before: str
    title: str
    type: Optional[TypeItem]
    overdue: bool
    additional_cost: str
    actual_end_time: Optional[ActualEndTimeItem]
    id: str
    actual_start_time: Optional[ActualStartTimeItem]
    group: Optional[GroupItem]
    owner: Optional[OwnerItem]
    created_time: CreatedTime
    associated_entity: str
    priority: Optional[PriorityItem]
    created_by: CreatedBy
    due_by_time: Optional[DueByTimeItem]
    scheduled_end_time: Optional[ScheduledEndTimeItem]
    marked_owner: Any
    marked_group: Any
    site: Any
    baseURL: str
    estimated_effort: EstimatedEffort
    issitevisit: bool
    account: Optional[AccountItem]
    scheduled_start_time: Optional[ScheduledStartTimeItem]
    status: Status

    def representation(self):
        return {
            "id": self.id,
            "title": self.title
        }


class Model(BaseModel):
    response_status: List[ResponseStatu]
    list_info: ListInfo
    tasks: List[Task]
