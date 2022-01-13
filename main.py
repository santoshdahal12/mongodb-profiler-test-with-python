""" Run the following to test the scenario"""
from mongodb_profiler_test_with_python.create_source_file import write_records_to_file
from mongodb_profiler_test_with_python.db_manager import insert_bulk, fine_by_id, fine_by_date

if "__main__":
    """
    1. generate a million record
    2. do bulk insert
    """
    # uncomment below function to create 500K or more records"
    # write_records_to_file()
    # insert_bulk()

    record = fine_by_id('affb06c6-1319-42b8-8132-2690919301dc')
    fine_by_date(record['date']['created'])
