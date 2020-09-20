import statistics
import dateutil.parser


def create_report(analysis, dates, transfer, hours_delta, desired_hours) -> dict:

    def _get_text(transfer, hours_delta, desired_hours):
        if transfer[0] > 0:
            return """\
                Unfortunately, you have failed to meet your target goal of 
                <b>{0}</b> hrs/week by {1} hours. Therefore, an amount of <b>{2}</b> will be 
                withdrawn from your account!
            """.format(desired_hours, round(hours_delta, 2), transfer[1])
        else:
            return """\
                Congratulations! You have achieved your target goal of 
                <b>{0}</b> hrs/week by {1} hours. Therefore, an amount of <b>{2}</b> will be 
                deposited to your account!
            """.format(desired_hours, hours_delta, transfer[1] + " (currently)")#"$0 (currently)")

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

    body = """\
        <html><head></head><body><p>
            <br>{0}<br>{1}{2}<br>{3}<br><br>{4}
        </p></body></html>
    """.format(greeting, tab, text, analysis_str, closing)

    return {
        "subject" : subject,
        "body"    : body
    }


def analyze_data(data: dict, dates, desired_hours: float, day_range: int,
                 transfer_amount: float) -> dict:

    def color(item, hours: float, desired_hours: float) -> str:
        c = {
            "green" : "rgb(106, 168, 79)",
            "red"   : "rgb(244, 102, 102)"
        }
        valence = c["green"] if hours >= desired_hours else c["red"]
        span = "<span style='background-color: {}'>".format(valence)
        return span + str(item) + "</span>"

    def _mSec_to_hours(ms: int) -> float:
        return round((ms/60000) / 60, 2)

    def _parse_ISO8601(datestring: str):
        return dateutil.parser.parse(datestring)

    def _transfer_amount(total_hours: float, desired_hours: float,
                         transfer_amount: float) -> float:
        '''
        # TODO
        and for retrieving money when worked e.g. 60 hours.. maybe have a log
        of how much money has been transferred so can't go over total amount
        '''
        if tot_hours >= desired_hours:
            return 0
        else:
            # vielleicht log?
            # return round(transfer_amount*(.95**total_hours), 2)
            return round(transfer_amount+(.0003125*(-total_hours**3)),2)

    # def _return_date_formated(ISO8601data) -> str:
    #    # return 'Thursday 11. June 2020 16:26' e.g.
    #    return ISO8601data.strftime("%A %d. %B %Y %H:%M")

    analysis = dict()
    my_projects = ["h4l", "floorioperations"]
    data_detailed_all_projekts = data["reportDetailed"]["data"]
    ## Filter projects: H4L and Floori Operations
    data_detailed = list(filter(
        lambda x: x["project"] is not None 
        and x["project"].lower().replace(" ", "")
        in my_projects, data_detailed_all_projekts))
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

    # end_datetimes = list(map(lambda x: x["end"] , data_detailed))

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
    analysis["Total Entries"] = str(len(data_detailed))
    analysis["{}Number of Projects".format(tab)] = str(len(projects))

    t_amount = _transfer_amount(tot_hours, desired_hours, transfer_amount)
    transfer = [t_amount, color("$" + str(t_amount), tot_hours, desired_hours)]
    hours_delta = round(abs(desired_hours - tot_hours), 2)

    return create_report(analysis, dates, transfer, hours_delta,
                         desired_hours), t_amount
