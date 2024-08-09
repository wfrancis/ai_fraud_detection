from datetime import date
from typing import List


class Job:
    def __init__(self, job_id: str, description: str, store_id: str, start_date: date, ship_to: str, lot_suite: str,
                 work_order: str, labor_total: float, labor_items: List[dict]):
        self.job_id = job_id
        self.description = description
        self.store_id = store_id
        self.start_date = start_date
        self.ship_to = ship_to
        self.lot_suite = lot_suite
        self.work_order = work_order
        self.labor_total = labor_total
        self.labor_items = labor_items  # List of labor items (dicts with QTY and description)


class Installer:
    def __init__(self, installer_id: str, branch: str, weekly_earnings: float):
        self.installer_id = installer_id
        self.branch = branch
        self.weekly_earnings = weekly_earnings


class SchedulerConfig:
    def __init__(self, branch: str, date: date, min_single_job_pay: float, max_jobs: int, job_assign_mode: str,
                 min_clustered_pay: float):
        self.branch = branch
        self.date = date
        self.min_single_job_pay = min_single_job_pay
        self.max_jobs = max_jobs
        self.job_assign_mode = job_assign_mode
        self.min_clustered_pay = min_clustered_pay
