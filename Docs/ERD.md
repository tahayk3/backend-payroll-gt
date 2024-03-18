# Diagrama de Entidad-Relación (ERD) Sistema  de nominas T consulting, S.A

## Entidadades

### Company(empresa)
- id (PK): Identificador único 
- name  : Nombre de la empresa
- phone  : Telefono de la empresa
- description  : Breve descripcion de la empresa
- address  : Direccion de la empresa
- picture  : Logo de la empresa
- is_active  : Estado de la empresa
- created_at  : Fecha de registro


### User(Usuario)
- id (PK): Identificador único 
- email  : correo del usuario
- USERNAME_FIELD  : campo que sera el username
- REQUIRED_FIELDS : campos que son obligatorios
- role  : rol del usuario
- picture  : avatar del usuario
- password  : contrasena del usuario
- company : empresa a la que pertenece el usuario
- is_active  : estado del usualrio
- is_default_password  : si es un password generico

## Relaciones
- Un usuario debe pertenecer a una empresa

### Department(Departamento de trabajo)
- id (PK): Identificador único 
- name  : Nombre del departamento
- description  : breve descripcion del departamento
- company : identifcador de empresa
- is_active  : estado del departamento


## Relaciones
- Un departamento debe pertencer a una empresa

### JobPosition(puesto de trabajo)
- id (PK): Identificador único 
- name  : nombre del puesto de trabajo
- description  : breve descripcion del puesto
- company : empresa a la que pertenece el puesto de trabajo
- is_active  : estado del puesto de trabajo


## Relaciones
- Un cargo debe pertencer a una empresa

### Employee(empleado)
- id (PK): Identificador único 
- first_name  : Nombres del empleado
- last_name  : Apellidos del empleado
- phone  : Telefono del empleado
- address  : Direccion del empleado
- picture  : Fotografia del empleado
- dpi  : Documento de idenficacion del empleado
- date_hiring  : fecha de contratacion del empleado
- date_completion  : fecha de terminacion de contrato
- birth_date  : fecha de nacimiento del emopleado
- gender  : genero del empleado
- base_salary  : salario base del empleado
- base_salary_initial  : salario inicial del empleado al ser contratado
- head_department  : si el empleado es jefe de departamento
- method_payment  : forma de pago al empleado
- bank  : banco de transaccion del empleado
- account_number  : numero de cuenta del uempleado
- department  : departamento al que pertenece el empleado
- job_position  : cargo del empleado
- user  : usuario del empleado
- company  : empresa del empleado
- is_active  : estado del empleado

## Relaciones
- Un empleado debe pertenecer a una empresa
- Un empleado debe pertenecer a un departamento
- Un empleado debe tener un cargo
- Un empleado debe tener un usuario


### EmployeeDocument(Documentos)
- id (PK): Identificador único 
- name  : Nombre del documento
- file  : archivo
- employee  : empleado al que pertenece el documento
- is_active  : estado del documento

## Relaciones
- Un documento debe pertenecer a un empleado

### FamilyMember(familiares)
- id (PK): Identificador único 
- first_name  : Nombres del familiar del empleado
- last_name  : Apellidos del familia del empleado
- relationship  : relacion con empleado
- gender  : genero del familiar
- phone  : Telefono del empleado
- employee  : Empleado al que pertenece
- is_active  : Estado del familiar
- created_at  : Fecha de creacion

## Relaciones
- Un familiar debe pertenecer a un empleado

### SalaryIncrease(incremento salarial)
- id (PK): Identificador único 
- employee  : Empleado del incremento
- amount  : monto del incremento
- reason  : razon dle incremento
- is_active  : Estado del incremento
- created_at  : Fecha de creacion del registro


## Relaciones
- Un incremento debe pertencer a un empleado

### RequestAbsence(Permisos)
- id (PK): Identificador único 
- employee  : Empleado del permiso
- company  : Empresa del permiso
- start_date  : Fecha de incio del permiso
- end_date  : Fin del permiso
- reason  : Razon del permiso
- status  : Estado del permiso
- is_active  : Si el permiso es vigente
- created_at  : Fecha de creacion


## Relaciones
- Un permiso debe pertenecer a un empleado
- Un permiso debe pertenecer a una empresa

### Image(Imagen)
- id (PK): Identificador único 
- picture  : imagen
- is_active  : estado de la imagen
- created_at  : fecha de creacion
- updated_at  : fecha de actualizancion

    

### File(Archivo)
- id (PK): Identificador único 
- file  : archivo
- is_active  : estdo del archivo
- created_at  : fehca de creacion
- updated_at  :


### PayrollPeriod(periodo de la nomina)
id (PK): Identificador único 
name  : nombre del periodo
start_date  : inicio del periodo
end_date  : fin del periodo
type  : tipo de periodo
company  : empresa a la que pertenece el periodo
is_open  : si esta abierto o cerrado

## Relaciones
- Un periodo debe pertenecer a una empresa

### Payroll
- id (PK): Identificador único 
- company  : empresa a la que pertenece la nomina
- payroll_period  : periodo a la que pertenece
- date_generated  : fecha de generacion de la nomina
- total  : total de la nomina
- is_open  : Si esta abierto
- is_active  : Estado de la nomina
- created_at  : Fecha de creacion


## Relaciones
- Una nomina debe pertenecer a una empresa
- Una nomina debe pertenecer a un periodo

### PayrollDeduction(Deducciones)
- id (PK): Identificador único 
- employee  : empleado al que pertenece la deduccion
- type_concept  : concepto de la deduccion
- quantity  : cantidad de deduccion
- amount  : monto
- reason  : razon de la deduccion
- total  : total de duccion
- date  : fecha de registro
- payroll_period  : periodo al que pertenece la deduccion

## Relaciones
- Una Deduccion debe pertenecer a una empresa
- Una Deduccion debe pertenecer a un periodo

### PayrollIncome (Ingresos)
- id (PK): Identificador único 
- employee  : empleado al que pertenece la Ingresos 
- type_concept  : concepto de la Ingresos 
- quantity  : cantidad de Ingresos 
- amount  : monto
- reason  : razon de la Ingresos 
- total  : total de duccion
- date  : fecha de registro
- payroll_period  : periodo al que pertenece la Ingresos 

## Relaciones
- Una Ingresos  debe pertenecer a una empresa
- Una DIngresos debe pertenecer a un periodo

### PayrollAccountingTransaction(Transacciones contables)
- id (PK): Identificador único 
- employee  : empleado al que pertenece la Transaccion
- type_concept  : concepto de la Transaccion
- quantity  : cantidad de Transaccion
- amount  : monto
- reason  : razon de la Transaccion
- total  : total de duccion
- date  : fecha de registro
- payroll_period  : periodo al que pertenece la Transaccion

## Relaciones
- Una Transaccion debe pertenecer a una empresa
- Una Transaccion debe pertenecer a un periodo


### TransferBank
- id (PK): Identificador único 
- employee  : empleado de la transferencia
- date  : fecha de transferencia
- bank  : nombre del banco
- account_number  : numero de cuenta bancaria
- reason  : razon de la cuenta bancaria
- amount  : monto
- is_active  : si esta activo
- created_at  : fecha de creacion
- payroll_period  : perido a la que pertenece

## Relaciones
- Una Transaccion debe pertenecer a una empresa
- Una Transaccion debe pertenecer a un periodo



### TransferCash
id (PK): Identificador único 
employee  : empleado a la que pertenece la transferencia
date  : fecha de transaccion
reason  : razon de la transferencia
amount  : monto
is_active  : estado del registro
created_at  : fecha de creacion
payroll_period  : periodo a la que pertenece


## Relaciones
- Una Transaccion debe pertenecer a una empresa
- Una Transaccion debe pertenecer a un periodo

### PayrollConcept
- id (PK): Identificador único 
- concept  : nombre del concept
- employee  : empleado que le pertenece le concepto
- payroll_period  : periodo a la que pertenece
- company  : empresa de a la que pertenece
- date  : fecha de ingreso
- reason  : razon del concepto
- overtime_minutes  : minutos  x horas extras
- public_holiday  : si es domingo o dia festivo
- sales  : total de ventas
- production  : total de produccion
- amount  : monto
- is_cancelled  : si esta cancelado
- is_active  : estado del concepto
- created_at  : fecha de creacion



## Relaciones
- Un concepto debe pertencer a un empleado
- Un concepto debe pertencer a una empresa
- un concepto debe pertencer a un periodo


### StorePurchase
- id (PK): Identificador único 
- date  : fecha de la compra
- total  : total
- cancelled : si esta cancelado
- biweekly  : si  es la primera quincena
- employee  : empleado de la compra
- company  : empresa 

## Relaciones