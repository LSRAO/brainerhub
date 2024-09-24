import pandas as pd
from app.crud import get_company_by_name, create_company, bulk_insert_employees

def process_and_insert_data(db, df):
    # df = pd.read_excel(file_path)
    companies = df['COMPANY_NAME'].unique()

    company_map = {}
    for company_name in companies:
        company = get_company_by_name(db, company_name)
        if not company:
            company = create_company(db, company_name)
        company_map[company_name] = company.id

    employee_data = [
        {
            'first_name': row['FIRST_NAME'],
            'last_name': row['LAST_NAME'],
            'phone_number': row['PHONE_NUMBER'],
            'salary': row['SALARY'],
            'manager_id': row['MANAGER_ID'] if pd.notna(row['MANAGER_ID']) else None,
            'department_id': row['DEPARTMENT_ID'] if pd.notna(row['DEPARTMENT_ID']) else None,
            'company_id': company_map[row['COMPANY_NAME']]
        }
        for _, row in df.iterrows()
    ]

    bulk_insert_employees(db, employee_data)
