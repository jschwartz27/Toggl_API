import statistics
import dateutil.parser


def create_report(analysis, dates, transfer, hours_delta, desired_hours) -> dict:

    def _get_text(transfer, hours_delta, desired_hours):
        if transfer[0] > 0:
            return """\
                Unfortunately, you have failed to meet your target goal of 
                <b>{0}</b> hrs/week by {1} hours. Therefore, an amount of <b>{2}</b> will be 
                withdrawn from your account!
            """.format(desired_hours, hours_delta, transfer[1])
        else:
            return "Good Job!"

    begin = "{}/{}/{}".format(dates[0].month, dates[0].day, dates[0].year)
    today = "{}/{}/{}".format(dates[1].month, dates[1].day, dates[1].year)
    subject = "Progress report ({}-{})".format(begin, today)
    tab = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    greeting = "Dear Yousef,"
    text = _get_text(transfer, hours_delta, desired_hours)
    analysis_str = "\n"
    for name in analysis:
        name_b = "<b>" + name + "</b>"
        analysis_str += "<br>{}".format(tab) + name_b + ": " + analysis[name] 
    closing = "Sincerely,<br>{}Your friendly AI overlord".format(tab)
    body = greeting + text + analysis_str + closing
    body = """\
        <html><head></head>
        <body>
            <p>
                <br>{0}<br>
                {1}{2}<br>{3}<br><br>{4}
            </p>
        </body>
        </html>
    """.format(greeting, tab, text, analysis_str, closing)

    return {
        "subject": subject,
        "body": body
    }


def analyze_data(data: dict, dates, desired_hours: float, day_range: int,
                 transfer_amount: float) -> dict:

    def color(item, hours: float, desired_hours: float) -> str:
        c = {
            "green": "rgb(106, 168, 79)",
            "red": "rgb(244, 102, 102)"
        }
        valence = c["green"] if hours >= desired_hours else c["red"]
        span = "<span style='background-color: {}'>".format(valence)
        return span + str(item) + "</span>"


    def _mSec_to_hours(ms: int) -> float:
        return round((ms/60000) / 60, 2)

    def _parse_ISO8601(datestring: str):
        return dateutil.parser.parse(datestring)

    def _transfer_amount(total_hours: float, desired_hours: float,
                         transfer_amount: float):
        '''
        # TODO
        and for retrieving money when worked e.g. 60 hours.. maybe have a log
        of how much money has been transferred so can't go over total amount
        '''
        if tot_hours >= desired_hours:
            return 0
        else:
            return round(transfer_amount*(.93**total_hours), 2)

    # def _return_date_formated(ISO8601data) -> str:
    #    # return 'Thursday 11. June 2020 16:26' e.g.
    #    return ISO8601data.strftime("%A %d. %B %Y %H:%M")

    analysis = dict()

    data_detailed = data["reportDetailed"]["data"]
    ms_per_day = dict()
    for datum in data_detailed:
        # ? What if working from 23:00 to 04:00? All hour will be for day
        # ? of start time
        day = str(_parse_ISO8601(datum["start"]).day)
        if day not in ms_per_day:    
            ms_per_day[day] = datum["dur"]
        else:
            ms_per_day[day] += datum["dur"]

    daily_mSecs = list(ms_per_day.values())
    tot_hours = _mSec_to_hours(sum(daily_mSecs))
    while len(daily_mSecs) < day_range:
        daily_mSecs.append(0)
    mean_hour_per_day = _mSec_to_hours(statistics.mean(daily_mSecs))
    stdev_hour_per_day = _mSec_to_hours(statistics.stdev(daily_mSecs))

    n_entries = len(data_detailed)
    end_datetimes = list(map(lambda x: x["end"] , data_detailed))

    unknown = ("", None)
    descriptions = list(set(map(lambda x: x["description"] , data_detailed)))
    projects = list(set(map(lambda x: x["project"] , data_detailed)))
    for i in [[descriptions, "No Description"], [projects, "Unnamed Project"]]:
        app = False
        for j in unknown:
            if j in i[0]:
                app = True
                i[0].remove(j)
        if app:
            i[0].append(i[1])

    # then also compare present data to all data,
    # get all data and compare last week to all
    # ? Maybe also email some graphs of data?

    tab = "&nbsp;&nbsp;&nbsp;&nbsp;"
    analysis["Total Time (hours)"] = color(tot_hours, tot_hours, desired_hours)
    analysis["{}Mean (hrs/day)".format(tab)] = str(mean_hour_per_day)
    analysis["{}Standard Deviation (hrs/day)".format(tab)] = str(stdev_hour_per_day)
    
    analysis["Total Entries"] = str(n_entries)
    analysis["{}Number of Porjects".format(tab)] = str(len(projects))

    t_amount = _transfer_amount(tot_hours, desired_hours, transfer_amount)
    transfer = [t_amount, color("$" + str(t_amount), tot_hours, desired_hours)]
    hours_delta = desired_hours - tot_hours

    return create_report(analysis, dates, transfer, hours_delta,
                         desired_hours), t_amount


def main():
    data = { "reportDetailed": {"data": [
        {'id': 1655327710, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'redline the SHI agreement', 'start': '2020-08-13T12:54:36-05:00', 'end': '2020-08-13T12:55:25-05:00', 'updated': '2020-08-13T12:55:25-05:00', 'dur': 49000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1639475254, 'pid': None, 'tid': None, 'uid': 4412058, 'description': '', 'start': '2020-07-30T10:42:02-05:00', 'end': '2020-07-30T11:15:13-05:00', 'updated': '2020-07-30T11:15:13-05:00', 'dur': 1991000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1629148930, 'pid': None, 'tid': None, 'uid': 4412058, 'description': 'R&S Flooring', 'start': '2020-07-21T17:25:14-05:00', 'end': '2020-07-21T17:25:15-05:00', 'updated': '2020-07-21T17:25:15-05:00', 'dur': 1000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583202044, 'pid': 155907675, 'tid': None, 'uid': 4412058, 'description': 'music', 'start': '2020-06-11T21:42:48-05:00', 'end': '2020-06-11T23:43:54-05:00', 'updated': '2020-06-11T23:43:55-05:00', 'dur': 7266000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Yousef 3.0', 'project_color': '0', 'project_hex_color': '#06a893', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583157155, 'pid': 155907675, 'tid': None, 'uid': 4412058, 'description': 'food', 'start': '2020-06-11T20:10:17-05:00', 'end': '2020-06-11T21:35:59-05:00', 'updated': '2020-06-11T21:36:15-05:00', 'dur': 5142000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Yousef 3.0', 'project_color': '0', 'project_hex_color': '#06a893', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': ['food']},
        {'id': 1583126568, 'pid': None, 'tid': None, 'uid': 4412058, 'description': 'pricing page edits', 'start': '2020-06-11T19:13:09-05:00', 'end': '2020-06-11T20:03:52-05:00', 'updated': '2020-06-11T20:03:53-05:00', 'dur': 3043000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583121035, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'Clear all recent email tasks + Jira tasks', 'start': '2020-06-11T19:03:17-05:00', 'end': '2020-06-11T19:12:59-05:00', 'updated': '2020-06-11T19:12:59-05:00', 'dur': 582000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583119062, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'lawyer stuff', 'start': '2020-06-11T18:36:43-05:00', 'end': '2020-06-11T19:00:43-05:00', 'updated': '2020-06-11T19:00:23-05:00', 'dur': 1440000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583083763, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'respond to Marc', 'start': '2020-06-11T17:58:43-05:00', 'end': '2020-06-11T18:18:28-05:00', 'updated': '2020-06-11T18:18:29-05:00', 'dur': 1185000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583048719, 'pid': 155907675, 'tid': None, 'uid': 4412058, 'description': 'figuring out flights with erik', 'start': '2020-06-11T17:04:14-05:00', 'end': '2020-06-11T17:58:38-05:00', 'updated': '2020-06-11T17:58:38-05:00', 'dur': 3264000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Yousef 3.0', 'project_color': '0', 'project_hex_color': '#06a893', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583034167, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'respond to Marc', 'start': '2020-06-11T16:44:59-05:00', 'end': '2020-06-11T17:04:03-05:00', 'updated': '2020-06-11T17:04:03-05:00', 'dur': 1144000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []},
        {'id': 1583031808, 'pid': None, 'tid': None, 'uid': 4412058, 'description': 'captains log', 'start': '2020-06-11T16:26:43-05:00', 'end': '2020-06-11T16:41:43-05:00', 'updated': '2020-06-11T16:43:23-05:00', 'dur': 900000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
    ]}}
    print(analyze_data(data))

if __name__ == "__main__":
    main()

'''
DATA_KEYS
"id", "pid", "tid", "uid", "description", "start", "end", "updated", "dur", "user",
"use_stop", "client", "project", "project_color", "project_hex_color", "task",
"billable", "is_billable", "cur", "tags"

'''
