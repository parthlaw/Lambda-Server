import enum


class ValidationResp(enum.Enum):
    Wrong_Phone="Wrong Phone Number"
    Wrong_PAN="Wrong PAN"
    EMPTY_NAME = "Full name is required"
