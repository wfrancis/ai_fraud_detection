from inscheduler.data_model import *

class Scheduler:
    def __init__(self):
        self.jobs = []
        self.installers = []

    def add_job(self, job: Job):
        self.jobs.append(job)

    def add_installer(self, installer: Installer):
        self.installers.append(installer)

    def load_installers(self, branch: str):
        # Load installers for the selected branch
        return [installer for installer in self.installers if installer.branch == branch]

    def load_weekly_earnings(self, installer_id: str):
        # Load weekly earnings for a given installer
        installer = next((inst for inst in self.installers if inst.installer_id == installer_id), None)
        return installer.weekly_earnings if installer else 0.0

    def display_job_summary(self):
        print("Job Summary:")
        for job in self.jobs:
            print(
                f"Job ID: {job.job_id}, Description: {job.description}, Store ID: {job.store_id}, Start Date: {job.start_date}, Total Pay: ${job.labor_total:.2f}")
        print(f"Total Number of Jobs: {len(self.jobs)}")
        print(f"Total Pay for the Day: ${sum(job.labor_total for job in self.jobs):.2f}\n")

    def display_installers(self, branch: str):
        print(f"Installers in Branch {branch}:")
        installers = self.load_installers(branch)
        for installer in installers:
            print(f"Installer ID: {installer.installer_id}, Weekly Earnings: ${installer.weekly_earnings:.2f}")
        print(f"Total Number of Installers in Branch {branch}: {len(installers)}\n")

    def display_installer_checklist(self, branch: str):
        print(f"Installer Checklist for Branch {branch}:")
        installers = self.load_installers(branch)
        for installer in installers:
            weekly_earnings = self.load_weekly_earnings(installer.installer_id)
            print(f"Installer ID: {installer.installer_id}, Weekly Earnings: ${weekly_earnings:.2f}")
        print("\n")

    def assign_jobs(self, config: SchedulerConfig):
        # Logic to assign jobs to installers based on the configuration
        available_installers = self.load_installers(config.branch)
        # Further logic to match jobs to installers based on the criteria
        pass