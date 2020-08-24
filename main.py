import argparse
import dateutil.parser
from toggl.TogglPy import Toggl

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


def get_args() -> object:
    parser = argparse.ArgumentParser(description="Key phrase search")
    parser.add_argument("-k", "--key", required=True, type=str,
                        help='cipher_key')
    parser.add_argument("-pdf", required=False, type=bool,
                        help="Option to attach detailed pdfs to your email")
    return parser.parse_args()


def retrieve_toggl_data(CREDENTIALS, get_pdfs: bool):

    def _mSec_to_min(ms: int) -> float:
        return ms/60000

    def _parse_ISO8601(datestring: str):
        return dateutil.parser.parse(datestring)

    toggl = Toggl()
    toggl.setAuthCredentials(CREDENTIALS["EMAIL"], CREDENTIALS["PASSWORD"])
    toggl.setAPIKey(CREDENTIALS["API_TOKEN"]) 
    workspace = toggl.getWorkspaces()[0]

    print("\nPROFILE DETAILS::")
    print("\tWorkspace Name      : {}".format(workspace["name"]))
    print("\tWorkspace ID        : {}".format(workspace["id"]))
    print("\tWorkspace api_token : {}\n".format(workspace["api_token"]))

    data = {
        'workspace_id' : workspace["id"],
        'since'        : '2020-05-16',
        'until'        : '2020-07-22'
    }

    the_D = {
        "reportSummary"  : toggl.getSummaryReport(data),
        "reportDetailed" : toggl.getDetailedReport(data),
        "reportWeekly"   : toggl.getWeeklyReport(data)
    }

    if get_pdfs:    
        toggl.getSummaryReportPDF(data, "summary-report.pdf")
        toggl.getDetailedReportPDF(data, "detailed-report.pdf")
        toggl.getWeeklyReportPDF(data, "weekly-report.pdf")

    return the_D


def analyze_data(data):
    for i in data[0]:
        print(i)
        print()
    
    quit()


def main():
    args = get_args()
    c = Cipher(args.key)

    creds = {
        i: c.decryptMessage(CREDENTIALS_ENCRYPT[i]) for i in CREDENTIALS_ENCRYPT
    }
    e_CREDS_deCRYpTed = {
        i: c.decryptMessage(EMAIL_CREDENTIALS[i]) for i in EMAIL_CREDENTIALS
    }

    the_D = retrieve_toggl_data(creds, args.pdf)
    results = analyze_data(the_D["reportDetailed"]["data"])
    email_functions.send(results["message"], args.pdf, e_CREDS_deCRYpTed)

if __name__ == "__main__":
    main()

'''
>>> yourdate.ctime()
'Thu Jun 11 16:26:43 2020'
>>> yourdate.strftime("%A %d. %B %Y %H:%M")
'Thursday 11. June 2020 16:26'
'''