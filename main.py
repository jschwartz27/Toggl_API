import argparse
from datetime import date, timedelta
from toggl.TogglPy import Toggl

import analyze
import email_functions
from cipher import Cipher

CREDENTIALS_ENCRYPT = {
    "EMAIL"     : "AEHls.qCJRPn1f&h",                
    "PASSWORD"  : "tP TzXlZ",                        
    "API_TOKEN" : "DXRy@cDbfhhzFR71ocH DlGaGU6W Vfb" 
}
EMAIL_CREDENTIALS = {
    "username" : "2EFaMLEEUDSpBZP",
    "password" : "87FltNEHGQHs7H73"
}


def get_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Key phrase search")
    parser.add_argument("-k", "--key", required=True, type=str,
                        help='cipher_key')
    parser.add_argument("-pdf", required=False, type=bool,
                        help="Option to attach detailed pdfs to your email")
    return parser.parse_args()


def retrieve_toggl_data(CREDENTIALS, get_pdfs: bool) -> dict:
    today = date.today()
    begin = today - timedelta(days=7)

    toggl = Toggl()
    toggl.setAuthCredentials(CREDENTIALS["EMAIL"], CREDENTIALS["PASSWORD"])
    toggl.setAPIKey(CREDENTIALS["API_TOKEN"]) 
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

    return the_D


def main() -> None:
    args = get_args()
    c = Cipher(args.key)

    creds = {
        i: c.decryptMessage(CREDENTIALS_ENCRYPT[i]) for i in CREDENTIALS_ENCRYPT
    }
    e_CREDS_deCRYpTed = {
        i: c.decryptMessage(EMAIL_CREDENTIALS[i]) for i in EMAIL_CREDENTIALS
    }

    the_D = retrieve_toggl_data(creds, args.pdf)
    analysis = analyze.analyze_data(the_D)
    # email_functions.send(analysis["message"], args.pdf, e_CREDS_deCRYpTed)

if __name__ == "__main__":
    main()

'''
>>> yourdate.ctime()
'Thu Jun 11 16:26:43 2020'
'''
