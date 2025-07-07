from datetime import date

account_template = [
    "AMRSPI/Template - Closed Accounts",
    "AMRSPI/Template - EQ+CA,FI/Family Account/DD",
    "AMRSPI/Template - EQ+CA,FI/Family Account/NotDD",
    "AMRSPI/Template - EQ+CA,FI/Single Account/DD",
    "AMRSPI/Template - EQ+CA,FI/Single Account/NotDD",
    "AMRSPI/Template - EQ+FI+CA/Family Account/DD",
    "AMRSPI/Template - EQ+FI+CA/Family Account/DD/Arrears",
    "AMRSPI/Template - EQ+FI+CA/Family Account/NotDD",
    "AMRSPI/Template - EQ+FI+CA/Family Account/NotDD/Arrears",
    "AMRSPI/Template - EQ+FI+CA/Single Account/DD",
    "AMRSPI/Template - EQ+FI+CA/Single Account/DD/Arrears",
    "AMRSPI/Template - EQ+FI+CA/Single Account/NotDD",
    "AMRSPI/Template - EQ+FI+CA/Single Account/NotDD/BBR",
    "AMRSPI/Template - EQ+FI+CA/Single Account/NotDD/BBR-LADDERED",
    "AMRSPI/Template - EQ+FI+CA/Single Account/NotDD/UnitedCap",
    "AMRSPI/Template - FI+CA,EQ/Family Account/DD",
    "AMRSPI/Template - FI+CA,EQ/Family Account/NotDD",
    "AMRSPI/Template - FI+CA,EQ/Single Account/DD",
    "AMRSPI/Template - FI+CA,EQ/Single Account/NotDD",
    "AMRSPI/Template - Junkyard",
    "AMRSPI/Template - Managed Hold Accounts",
    "AMRSPI/Template - Non Reconciled Accounts"
]

def _file_date():
    return date.today().strftime("%m/%d/%Y")

def non_managed_hold(account_id, name, start_date):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Bonaire>
    <RevportHeader CheckMInRequiredForUpdate="False"
        DeleteContactByOmission="False" FileDate="{_file_date()}"
        UpdateCommission="True" UpdateContactByType="True"/>
    <RevportBody DataType="Account">
<Account AccountType="Client Account" BusinessUnit="PI"
    BusinessWorkGroup="AMRSPI" ClientAccountId="{account_id}"
    ClientFirmId="Template - AMRSPI" ISOCurrency="USD"
    InceptionDate="{start_date}"
    Name="{name}"
    ShortName="{name}" StartDate="{start_date}" PortfolioBillingRecord="AMRSPI/Template - Managed Hold Accounts">
</Account>
</RevportBody>
<RevportTrailer DataType="Account" RecordCount="1"/>
</Bonaire>"""

def previous_template(account_id, name, start_date, template):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Bonaire>
    <RevportHeader CheckMInRequiredForUpdate="False"
        DeleteContactByOmission="False" FileDate="{_file_date()}"
        UpdateCommission="True" UpdateContactByType="True"/>
    <RevportBody DataType="Account">
<Account AccountType="Client Account" BusinessUnit="PI"
    BusinessWorkGroup="AMRSPI" ClientAccountId="{account_id}"
    ClientFirmId="Template - AMRSPI" ISOCurrency="USD"
    InceptionDate="{start_date}"
    Name="{name}"
    ShortName="{name}" StartDate="{start_date}" PortfolioBillingRecord="{template}">
</Account>
</RevportBody>
<RevportTrailer DataType="Account" RecordCount="1"/>
</Bonaire>"""

def previous_template_with_enddate(account_id, name, start_date, end_date, template):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Bonaire>
    <RevportHeader CheckMInRequiredForUpdate=""False""
        DeleteContactByOmission="False" FileDate="{_file_date()}"
        UpdateCommission="True" UpdateContactByType="True"/>
    <RevportBody DataType="Account">
<Account AccountType="Client Account" BusinessUnit="PI"
    BusinessWorkGroup="AMRSPI" ClientAccountId="{account_id}"
    ClientFirmId="Template - AMRSPI" ISOCurrency="USD"
    InceptionDate="{start_date}" EndDate={end_date}
    Name="{name}"
    ShortName="{name}" StartDate="{start_date}" PortfolioBillingRecord="{template}'>
</Account>
</RevportBody>
<RevportTrailer DataType="Account" RecordCount="1"/>
</Bonaire>"""

def previous_template_blank_end(account_id, name, start_date, template):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Bonaire>
    <RevportHeader CheckMInRequiredForUpdate="False"
        DeleteContactByOmission="False" FileDate="{_file_date()}"
        UpdateCommission="True" UpdateContactByType="True"/>
    <RevportBody DataType="Account">
<Account AccountType="Client Account" BusinessUnit="PIS"
    BusinessWorkGroup="AMRSPI" ClientAccountId="{account_id}"
    ClientFirmId="Template - AMRSPI" ISOCurrency="USD"
    InceptionDate="{start_date}" EndDate=
    Name="{name}"
    ShortName="{name}" StartDate="{start_date}" PortfolioBillingRecord="{template}">
</Account>
</RevportBody>
<RevportTrailer DataType="Account" RecordCount="1"/>
</Bonaire>"""

