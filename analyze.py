import dateutil.parser


def analyze_data(data: dict) -> dict:

    def _mSec_to_min(ms: int) -> float:
        return ms/60000

    def _parse_ISO8601(datestring: str):
        return dateutil.parser.parse(datestring)
    
    def _return_date_formated(ISO8601data) -> str:
        # return 'Thursday 11. June 2020 16:26' e.g.
        return ISO8601data.strftime("%A %d. %B %Y %H:%M")

    data_detailed = data["reportDetailed"]["data"]

    # ? I forget the key for the end time
    dates = list(map(lambda x: x["end"] , data))
    # ? or maybe just sort data by end date?
    # ? function also to just sum total time and compare to 40 h/week
    # and also number of projects
    # number of entries

    # then also compare present data to all data,
    # get all data and compare last week to all
    # ? Maybe also email some graphs of data?
    quit()
