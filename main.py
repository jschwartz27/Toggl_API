import app.analyze as analyze
import app.helper_functions as helper_functions
import app.email_function as email_function
import app.toggl_function as toggl_function
import app.venmo_function as venmo_function


def main() -> None:
    args = helper_functions.get_args()
    CREDENTIALS = helper_functions.load_yml("../toggl_creds")
    configs = helper_functions.load_yml("config")

    the_D = toggl_function.retrieve_toggl_data(CREDENTIALS["toggl"], args.pdf)
    print(the_D)
    quit()
    analysis = analyze.analyze_data(the_D)
    # email_function.send(analysis["message"], args.pdf, CREDENTIALS["email"])
    # venmo_function(configs["transfer_amount"], CREDENTIALS["venmo"])

if __name__ == "__main__":
    main()
