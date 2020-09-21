from toggl.TogglPy import Toggl
from datetime import date, timedelta


def retrieve_toggl_data(CREDENTIALS, get_pdfs: bool) -> dict:

    ### Get Dates ###
    today = date.today() - timedelta(days=1) # today == Sunday
    days_7 = today - timedelta(days=6)

    # beginning = date(2019, 2, 2)
    # Monday Sept 14, 2020
    # beginningOfPsychMod = date(2020, 9, 14)

    ### Initialize Toggl Auth ###
    toggl = Toggl()
    toggl.setAuthCredentials(CREDENTIALS["username"], CREDENTIALS["password"])
    toggl.setAPIKey(CREDENTIALS["api_token"]) 
    workspace = toggl.getWorkspaces()[0]

    print("\nPROFILE DETAILS::")                                          # ! REMOVE
    print("\tWorkspace Name      : {}".format(workspace["name"]))         # ! REMOVE
    print("\tWorkspace ID        : {}".format(workspace["id"]))           # ! REMOVE
    print("\tWorkspace api_token : {}\n".format(workspace["api_token"]))  # ! REMOVE

    details = {
        "workspace_id" : workspace["id"],
        "since"        : "{}-{}-{}".format(days_7.year, days_7.month, days_7.day),
        "until"        : "{}-{}-{}".format(today.year, today.month, today.day)
    }

    the_D = {  # ? Some of these might not be necessary
        # "reportSummary"  : toggl.getSummaryReport(details),  # !
        "reportDetailed" : toggl.getDetailedReport(details),
        # "reportWeekly"   : toggl.getWeeklyReport(details)
    }

    if get_pdfs:    
        toggl.getSummaryReportPDF(details,  "summary-report.pdf")
        toggl.getDetailedReportPDF(details, "detailed-report.pdf")
        toggl.getWeeklyReportPDF(details,   "weekly-report.pdf")

    return the_D, (days_7, today)

'''
>>> yourdate.ctime()
'Thu Jun 11 16:26:43 2020'
'''
