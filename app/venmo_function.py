from venmo_api import Client


def transfer_funds(amount: float, CREDENTIALS):
    assert (
        amount <= 20  # just in case ;)
        and isinstance(amount, (int, float))
        and not isinstance(amount, (bool, str))
    )
    # Get your access token. You will need to complete the 2FA process
    # access_token = Client.get_access_token(username=CREDENTIALS["username"],
    #                                       password=CREDENTIALS["password"])

    venmo = Client(access_token=CREDENTIALS["access_token"])
    print("logged in")
    def callback(transactions_list):
        for transaction in transactions_list:
            print(transaction)
    #venmo.user.get_user_transactions(user_id=CREDENTIALS["usernameII"],
    #                                 callback=callback)
    quit()
    venmo.payment.send_money(amount, "thanks for the 🍔", CREDENTIALS["usernameII"])
    print("payement 'sent'?")
    # log_out_str = "{} {}".format(CREDENTIALS["username"],
    #                             CREDENTIALS["access_token"])
    venmo.log_out(CREDENTIALS["access_token"])
    print("Success")

    # ? is there a way to check balance first??
    # ? Does there need to be money in venmo first or does it withdraw
    # venmo.log_out("Bearer a40fsdfhsfhdsfjhdkgljsdglkdsfj3j3i4349t34j7d")
    # venmo.payment.send_money(13.68, "thanks for the 🍔", "1122334455667")
