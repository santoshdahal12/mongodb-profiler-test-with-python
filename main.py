""" Run the following to test the scenario"""
from mongodb_with_python_bulk_insert.create_source_file import write_records_to_file
from mongodb_with_python_bulk_insert.db_manager import insert_bulk, fine_by_id

if "__main__":
    """
    1. generate a million record
    2. do bulk insert
    """
    # write_records_to_file()
    # insert_bulk()
    print(fine_by_id('1f90465e-8246-4738-8957-04a73cb9e21b'))
