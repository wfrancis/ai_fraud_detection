from inscheduler.data_model import *


def generate_simulated_data(scheduler):
    # Add Flooring Jobs
    scheduler.add_job(Job(
        job_id="J001",
        description="Install hardwood flooring",
        store_id="S001",
        start_date=date(2024, 8, 8),
        ship_to="123 Main St",
        lot_suite="Lot 1",
        work_order="WO1234",
        labor_total=1200.00,
        labor_items=[{"QTY": 100, "description": "Hardwood floor installation"}]
    ))

    scheduler.add_job(Job(
        job_id="J002",
        description="Install carpet flooring",
        store_id="S002",
        start_date=date(2024, 8, 8),
        ship_to="456 Elm St",
        lot_suite="Lot 2",
        work_order="WO1235",
        labor_total=800.00,
        labor_items=[{"QTY": 150, "description": "Carpet installation"}]
    ))

    scheduler.add_job(Job(
        job_id="J003",
        description="Install vinyl flooring",
        store_id="S003",
        start_date=date(2024, 8, 9),
        ship_to="789 Oak St",
        lot_suite="Lot 3",
        work_order="WO1236",
        labor_total=900.00,
        labor_items=[{"QTY": 200, "description": "Vinyl floor installation"}]
    ))

    scheduler.add_job(Job(
        job_id="J004",
        description="Install laminate flooring",
        store_id="S004",
        start_date=date(2024, 8, 10),
        ship_to="101 Pine St",
        lot_suite="Lot 4",
        work_order="WO1237",
        labor_total=1000.00,
        labor_items=[{"QTY": 120, "description": "Laminate floor installation"}]
    ))

    scheduler.add_job(Job(
        job_id="J005",
        description="Install tile flooring",
        store_id="S005",
        start_date=date(2024, 8, 10),
        ship_to="202 Maple St",
        lot_suite="Lot 5",
        work_order="WO1238",
        labor_total=1100.00,
        labor_items=[{"QTY": 80, "description": "Tile floor installation"}]
    ))

    # Add more flooring jobs if needed to increase complexity
    for i in range(6, 16):
        scheduler.add_job(Job(
            job_id=f"J00{i}",
            description="Install engineered wood flooring",
            store_id=f"S00{i}",
            start_date=date(2024, 8, 11),
            ship_to=f"{300 + i} Birch St",
            lot_suite=f"Lot {i}",
            work_order=f"WO123{i + 3}",
            labor_total=950.00 + i * 20,
            labor_items=[{"QTY": 130 + i * 10, "description": "Engineered wood floor installation"}]
        ))

    # Add Installers
    scheduler.add_installer(Installer(
        installer_id="I001",
        branch="Branch1",
        weekly_earnings=2000.00
    ))

    scheduler.add_installer(Installer(
        installer_id="I002",
        branch="Branch1",
        weekly_earnings=1500.00
    ))

    scheduler.add_installer(Installer(
        installer_id="I003",
        branch="Branch2",
        weekly_earnings=1800.00
    ))

    scheduler.add_installer(Installer(
        installer_id="I004",
        branch="Branch2",
        weekly_earnings=1700.00
    ))

    scheduler.add_installer(Installer(
        installer_id="I005",
        branch="Branch3",
        weekly_earnings=1600.00
    ))

    # Add more installers if needed to increase complexity
    for i in range(6, 16):
        scheduler.add_installer(Installer(
            installer_id=f"I00{i}",
            branch=f"Branch{i % 3 + 1}",
            weekly_earnings=1200.00 + i * 50
        ))