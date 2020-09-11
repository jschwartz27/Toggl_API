from toggl.TogglPy import Toggl
from datetime import date, timedelta


def retrieve_toggl_data(CREDENTIALS, get_pdfs: bool) -> dict:
    today = date.today()
    begin = today - timedelta(days=90)
    years_5 = date(2019, 2, 2)
    toggl = Toggl()
    toggl.setAuthCredentials(CREDENTIALS["username"], CREDENTIALS["password"])
    toggl.setAPIKey(CREDENTIALS["api_token"]) 
    workspace = toggl.getWorkspaces()[0]

    print("\nPROFILE DETAILS::")
    print("\tWorkspace Name      : {}".format(workspace["name"]))
    print("\tWorkspace ID        : {}".format(workspace["id"]))
    print("\tWorkspace api_token : {}\n".format(workspace["api_token"]))

    details = {
        "workspace_id" : workspace["id"],
        "since"        : "{}-{}-{}".format(begin.year, begin.month, begin.day),
        "until"        : "{}-{}-{}".format(today.year, today.month, today.day)
    }

    the_D = {
        "reportSummary"  : toggl.getSummaryReport(details),
        "reportDetailed" : toggl.getDetailedReport(details),
        "reportWeekly"   : toggl.getWeeklyReport(details)
    }

    if get_pdfs:    
        toggl.getSummaryReportPDF(details,  "summary-report.pdf")
        toggl.getDetailedReportPDF(details, "detailed-report.pdf")
        toggl.getWeeklyReportPDF(details,   "weekly-report.pdf")

    return the_D, (begin, today)

'''
>>> yourdate.ctime()
'Thu Jun 11 16:26:43 2020'
'''
