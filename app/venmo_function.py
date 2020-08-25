from venmo_api import Client


def transfer_funds(amount: float):
    # Get your access token. You will need to complete the 2FA process
    access_token = Client.get_access_token(username='myemail@random.com',
                                           password='your password')
    venmo = Client(access_token=access_token)

    # Search for users. You get 50 results per page.
    users = venmo.user.search_for_users(query="Peter",
                                        page=2)
    for user in users:
        print(user.username)

    '''# Or, you can pass a callback to make it multi-threaded
    def callback(users):
        for user in users:
            print(user.username)
        venmo.user.search_for_users(query="peter",
                                    callback=callback,
                                    page=2,
                                    count=10)'''


def main():
	transfer_funds(5)	

if __name__ == '__main__':
	main()
