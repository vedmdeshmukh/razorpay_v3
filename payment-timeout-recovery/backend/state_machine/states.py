from enum import Enum

class PaymentState(str, Enum):
    CREATED = "CREATED"
    PROCESSING = "PROCESSING"
    UNKNOWN = "UNKNOWN"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
