from venmo_api import Client


def transfer_funds(amount: float, CREDENTIALS):
    # Get your access token. You will need to complete the 2FA process
    # access_token = Client.get_access_token(username=CREDENTIALS["username"],
    #                                       password=CREDENTIALS["password"])

    venmo = Client(access_token=CREDENTIALS["access_token"])
    # ! try except with error output

    quit()
    # ! is there a way to check balance first??
    # ? Does there need to be money in venmo first or does it withdraw
    # venmo.payment.send_money(amount, "motivation money", "MY NUMBA or profile??")

    log_out_str = "{} {}".format(CREDENTIALS["username"],
                                 CREDENTIALS["access_token"])
    # venmo.log_out("Bearer a40fsdfhsfhdsfjhdkgljsdglkdsfj3j3i4349t34j7d")
    venmo.log_out(log_out_str)
    # venmo.payment.send_money(13.68, "thanks for the 🍔", "1122334455667")
