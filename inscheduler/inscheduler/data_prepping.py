from inscheduler.scheduler import Scheduler
from inscheduler.sim_data import *

if __name__ == "__main__":
    # Example instantiation and usage
    scheduler = Scheduler()

    # Add some jobs and installers
    generate_simulated_data(scheduler)

    # Set up the scheduling configuration
    config = SchedulerConfig(branch="Branch1", date=date(2024, 8, 8), min_single_job_pay=100.00, max_jobs=5,
                             job_assign_mode="Priority", min_clustered_pay=300.00)

    # Assign jobs
    scheduler.assign_jobs(config)