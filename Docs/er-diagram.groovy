Table Company{
  id integer [primary key]
    name  varchar
    phone  varchar
    description  varchar
    address  varchar
    picture  varchar
    is_active  boolean
    created_at  timestamp
}

Table User{
    id integer [primary key]
    email  varchar
    USERNAME_FIELD  varchar
    REQUIRED_FIELDS varchar
    role  varchar
    picture  varchar
    password  varchar
    company  integer
    is_active  boolean
    is_default_password  boolean
}

Ref: Company.id < User.company

Table Department{
    id integer [primary key]
    name  varchar
    description  varchar
    company  integer
    is_active  boolean
}

Ref: Company.id < Department.company

Table JobPosition{
    id integer [primary key]
    name  varchar
    description  varchar
    company  integer
    is_active  boolean
}

Ref: Company.id < JobPosition.company

Table Employee{
    id integer [primary key]
    first_name  varchar
    last_name  varchar
    phone  varchar
    address  varchar
    picture  varchar
    dpi  varchar
    date_hiring  timestamp
    date_completion  timestamp
    birth_date  timestamp
    gender  varchar
    base_salary  integer
    base_salary_initial  integer
    head_department  boolean
    method_payment  varchar
    bank  varchar
    account_number  varchar
    department  integer
    job_position  integer
    user  integer
    company  integer
    is_active  boolean
}

Ref: Company.id < Employee.company
Ref: Department.id < Employee.department
Ref: JobPosition.id < Employee.job_position
Ref: User.id < Employee.user

Table EmployeeDocument{
    id integer [primary key]
    name  varchar
    file  varchar
    employee  integer
    is_active  boolean
}

Ref: Employee.id < EmployeeDocument.employee

Table FamilyMember{
    id integer [primary key]
    first_name  varchar
    last_name  varchar
    relationship  varchar
    gender  varchar
    phone  varchar
    employee  integer
    is_active  boolean
    created_at  timestamp
}

Ref: Employee.id < FamilyMember.employee

Table SalaryIncrease{
    id integer [primary key]
    employee  integer
    amount  integer
    reason  varchar
    is_active  boolean
    created_at  timestamp
}

Ref: Employee.id < SalaryIncrease.employee

Table RequestAbsence{
     id integer [primary key]
    employee  integer
    company  integer
    start_date  timestamp
    end_date  timestamp
    reason  varchar
    status  varchar
    is_active  boolean
    created_at  timestamp
}

Ref: Employee.id < RequestAbsence.employee
Ref: Company.id < RequestAbsence.company

Table PayrollImage{
    id integer [primary key]
    picture  varchar
    is_active  boolean
    created_at  timestamp
    updated_at  timestamp
}
    

Table PayrollFile{
    id integer [primary key]
    file  varchar
    is_active  boolean
    created_at  timestamp
    updated_at  timestamp
}

Table PayrollPeriod{
    id integer [primary key]
    name  varchar
    start_date  timestamp
    end_date  timestamp
    type  varchar
    company  integer
    is_open  boolean
}
Ref: Company.id < PayrollPeriod.company

Table Payroll{
    id integer [primary key]
    company  integer
    payroll_period  integer
    date_generated  timestamp
    total  integer
    is_open  boolean
    is_active  boolean
    created_at  timestamp
}

Ref: Company.id < Payroll.company
Ref: PayrollPeriod.id < Payroll.payroll_period

Table PayrollDeduction{
    id integer [primary key]
    employee  integer
    type_concept  varchar
    quantity  integer
    amount  integer
    reason  varchar
    total  integer
    date  timestamp
    payroll_period  integer
}

Ref: Employee.id < PayrollDeduction.employee
Ref: PayrollPeriod.id < PayrollDeduction.payroll_period

Table PayrollIncome{
    id integer [primary key]
    employee  integer
    type_concept  varchar
    quantity  integer
    amount  integer
    reason  varchar
    total  integer
    date  timestamp
    payroll_period  integer
}

Ref: Employee.id < PayrollIncome.employee
Ref: PayrollPeriod.id < PayrollIncome.payroll_period

Table PayrollAccountingTransaction{
    id integer [primary key]
    employee  integer
    type_concept  varchar
    quantity  integer
    amount  integer
    reason  varchar
    total  integer
    date  timestamp
    payroll_period  integer

}

Ref: Employee.id < PayrollAccountingTransaction.employee
Ref: PayrollPeriod.id < PayrollAccountingTransaction.payroll_period

Table TransferBank{
    id integer [primary key]
    employee  integer
    date  timestamp
    bank  varchar
    account_number  varchar
    reason  varchar
    amount  integer
    is_active  boolean
    created_at  timestamp
    payroll_period  integer
}


Ref: Employee.id < TransferBank.employee
Ref: PayrollPeriod.id < TransferBank.payroll_period

Table TransferCash{
    id integer [primary key]
    employee  integer
    date  timestamp
    reason  varchar
    amount  integer
    is_active  boolean
    created_at  timestamp
    payroll_period  integer
}

Ref: Employee.id < TransferCash.employee
Ref: PayrollPeriod.id < TransferCash.payroll_period

Table PayrollConcept{
    id integer [primary key]
    concept  varchar
    employee  integer
    payroll_period  integer
    company  integer
    date  timestamp
    reason  varchar
    overtime_minutes  integer
    public_holiday  boolean
    sales  integer
    production  integer
    amount  integer
    is_cancelled  boolean
    is_active  boolean
    created_at  timestamp

}

Ref: Employee.id < PayrollConcept.employee
Ref: PayrollPeriod.id < PayrollConcept.payroll_period
Ref: Company.id < PayrollConcept.company

Table StorePurchase{
  id integer [primary key]
  date  timestamp
  total  integer
  cancelled  boolean
  biweekly  boolean
  employee  integer
  company  integer
}

Ref: Employee.id < StorePurchase.employee
Ref: Company.id < StorePurchase.company