#!/usr/bin/env python3
"""
MySQL CSV Import Script - Generated by CSViper

This script imports CSV data into a MySQL database using pre-generated SQL scripts.

Original CSV: test_data_modified.csv
Generated on: 2025-06-23 03:00:12
"""

import os
import sys
import click

# Import the shared functionality from csviper package
try:
    from csviper.import_executor import ImportExecutor
except ImportError:
    # Fallback for standalone scripts - add the parent directory to path
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
    from csviper.import_executor import ImportExecutor


@click.command()
@click.option('--env_file_location', type=click.Path(),
              help='Path to .env file (auto-detected if not specified)')
@click.option('--csv_file', required=True, type=click.Path(),
              help='Path to CSV file to import')
@click.option('--db_schema_name', required=False,
              help='Database schema/database name (can be set via DB_SCHEMA env var)')
@click.option('--table_name', required=False,
              help='Table name for the imported data (can be set via DB_TABLE env var)')
@click.option('--trample', is_flag=True, default=False,
              help='Overwrite existing table data')
def main(env_file_location, csv_file, db_schema_name, table_name, trample):
    """
    Import CSV data into MySQL database using pre-generated SQL scripts.
    
    This script was generated by CSViper for the CSV file: test_data_modified.csv
    """
    try:
        # Load and validate configuration
        db_config, db_schema_name, table_name, metadata = ImportExecutor.load_and_validate_config(
            env_file_location, csv_file, db_schema_name, table_name, 'test_data_modified.metadata.json', use_colors=False
        )
        
        # Validate CSV header
        expected_columns = metadata['original_column_names']
        ImportExecutor.validate_csv_header(csv_file, expected_columns, use_colors=False)
        
        # Check debug mode
        debug_mode = db_config.get('DEBUG', '').lower() in ('true', '1', 'yes', 'on')
        if debug_mode:
            click.echo("Debug mode enabled")
        
        click.echo(f"Importing {os.path.basename(csv_file)} into MySQL database")
        click.echo(f"Schema: {db_schema_name}, Table: {table_name}")
        
        if trample:
            click.echo("Warning: --trample flag is set. Existing table data will be overwritten.")
        
        # Execute MySQL import using the shared executor
        ImportExecutor.execute_mysql_import(
            db_config, db_schema_name, table_name, csv_file, trample, 
            'test_data_modified.create_table_mysql.sql', 'test_data_modified.import_data_mysql.sql'
        )
        
        click.echo("✓ MySQL import completed successfully!")
        
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
