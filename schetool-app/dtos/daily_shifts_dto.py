from dataclasses import dataclass
from datetime import date, time


@dataclass
class DailyShiftsDto:
    shift_id: int
    shift_day: date
    shift_start_time: time
    shift_end_time: time
    shift_employee: int
    shift_schedule: int
