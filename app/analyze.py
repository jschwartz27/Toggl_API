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
    n_entries = len(data_detailed)
    end_datetimes = list(map(lambda x: x["end"] , data_detailed))
    descriptions = list(set(map(lambda x: x["description"] , data_detailed)))
    # descriptions.remove(None)
    projects = list(set(map(lambda x: x["project"] , data_detailed)))
    # projects.remove(None)
    # duration in minutes
    dur = _mSec_to_min(sum(list(map(lambda x: x["dur"] , data_detailed))))

    # ? or maybe just sort data by end date?
    # ? function also to just sum total time and compare to 40 h/week
    # and also number of projects

    # then also compare present data to all data,
    # get all data and compare last week to all
    # ? Maybe also email some graphs of data?


'''
"id", "pid", "tid", "uid", "description", "start", "end", "updated", "dur", "user",
"use_stop", "client", "project", "project_color", "project_hex_color", "task",
"billable", "is_billable", "cur", "tags"

{'id': 1655327710, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'redline the SHI agreement', 'start': '2020-08-13T12:54:36-05:00', 'end': '2020-08-13T12:55:25-05:00', 'updated': '2020-08-13T12:55:25-05:00', 'dur': 49000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1639475254, 'pid': None, 'tid': None, 'uid': 4412058, 'description': '', 'start': '2020-07-30T10:42:02-05:00', 'end': '2020-07-30T11:15:13-05:00', 'updated': '2020-07-30T11:15:13-05:00', 'dur': 1991000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1629148930, 'pid': None, 'tid': None, 'uid': 4412058, 'description': 'R&S Flooring', 'start': '2020-07-21T17:25:14-05:00', 'end': '2020-07-21T17:25:15-05:00', 'updated': '2020-07-21T17:25:15-05:00', 'dur': 1000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583202044, 'pid': 155907675, 'tid': None, 'uid': 4412058, 'description': 'music', 'start': '2020-06-11T21:42:48-05:00', 'end': '2020-06-11T23:43:54-05:00', 'updated': '2020-06-11T23:43:55-05:00', 'dur': 7266000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Yousef 3.0', 'project_color': '0', 'project_hex_color': '#06a893', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583157155, 'pid': 155907675, 'tid': None, 'uid': 4412058, 'description': 'food', 'start': '2020-06-11T20:10:17-05:00', 'end': '2020-06-11T21:35:59-05:00', 'updated': '2020-06-11T21:36:15-05:00', 'dur': 5142000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Yousef 3.0', 'project_color': '0', 'project_hex_color': '#06a893', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': ['food']}
{'id': 1583126568, 'pid': None, 'tid': None, 'uid': 4412058, 'description': 'pricing page edits', 'start': '2020-06-11T19:13:09-05:00', 'end': '2020-06-11T20:03:52-05:00', 'updated': '2020-06-11T20:03:53-05:00', 'dur': 3043000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583121035, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'Clear all recent email tasks + Jira tasks', 'start': '2020-06-11T19:03:17-05:00', 'end': '2020-06-11T19:12:59-05:00', 'updated': '2020-06-11T19:12:59-05:00', 'dur': 582000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583119062, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'lawyer stuff', 'start': '2020-06-11T18:36:43-05:00', 'end': '2020-06-11T19:00:43-05:00', 'updated': '2020-06-11T19:00:23-05:00', 'dur': 1440000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583083763, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'respond to Marc', 'start': '2020-06-11T17:58:43-05:00', 'end': '2020-06-11T18:18:28-05:00', 'updated': '2020-06-11T18:18:29-05:00', 'dur': 1185000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583048719, 'pid': 155907675, 'tid': None, 'uid': 4412058, 'description': 'figuring out flights with erik', 'start': '2020-06-11T17:04:14-05:00', 'end': '2020-06-11T17:58:38-05:00', 'updated': '2020-06-11T17:58:38-05:00', 'dur': 3264000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Yousef 3.0', 'project_color': '0', 'project_hex_color': '#06a893', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583034167, 'pid': 155907692, 'tid': None, 'uid': 4412058, 'description': 'respond to Marc', 'start': '2020-06-11T16:44:59-05:00', 'end': '2020-06-11T17:04:03-05:00', 'updated': '2020-06-11T17:04:03-05:00', 'dur': 1144000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': 'Floori Operations', 'project_color': '0', 'project_hex_color': '#e36a00', 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
{'id': 1583031808, 'pid': None, 'tid': None, 'uid': 4412058, 'description': 'captains log', 'start': '2020-06-11T16:26:43-05:00', 'end': '2020-06-11T16:41:43-05:00', 'updated': '2020-06-11T16:43:23-05:00', 'dur': 900000, 'user': 'Yousef', 'use_stop': True, 'client': None, 'project': None, 'project_color': '0', 'project_hex_color': None, 'task': None, 'billable': None, 'is_billable': False, 'cur': None, 'tags': []}
'''
