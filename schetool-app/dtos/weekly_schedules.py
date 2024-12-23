from dataclasses import dataclass
from datetime import date


@dataclass
class WeeklySchedulesDto:
    schedule_id: int
    schedule_start_day: date
    schedule_end_day: date

    @staticmethod
    def from_row(row):
        return WeeklySchedulesDto(*row) if row else None
