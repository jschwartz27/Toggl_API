from venmo_api import Client


def transfer_funds(amount: float, CREDENTIALS):
    # Get your access token. You will need to complete the 2FA process
    # access_token = Client.get_access_token(username=CREDENTIALS["username"],
    #                                       password=CREDENTIALS["password"])

    venmo = Client(access_token=CREDENTIALS["access_token"])

    # Search for users. You get 50 results per page.
    users = venmo.user.search_for_users(query="Peter",
                                        page=2)
    for user in users:
        print(user.username)
    quit()
    '''# Or, you can pass a callback to make it multi-threaded
    def callback(users):
        for user in users:
            print(user.username)
        venmo.user.search_for_users(query="peter",
                                    callback=callback,
                                    page=2,
                                    count=10)'''
    venmo.log_out("Bearer a40fsdfhsfhdsfjhdkgljsdglkdsfj3j3i4349t34j7d")
    # venmo.payment.send_money(13.68, "thanks for the 🍔", "1122334455667")
