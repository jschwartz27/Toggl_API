import yaml
import argparse

import app.analyze as analyze
import app.email_function as email_function
import app.toggl_function as toggl_function
import app.venmo_function as venmo_function


def load_yml(filename: str):
    with open(filename + ".yml") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def get_args() -> object:
    parser = argparse.ArgumentParser(description="Cipher key and helper arguments")
    # parser.add_argument("-key", required=True, type=str,
    #                    help='cipher_key')
    parser.add_argument("-pdf", required=False, type=bool,
                        help="Option to attach detailed pdfs to your email")
    return parser.parse_args()


def main() -> None:
    CREDENTIALS = load_yml("../toggl_creds")
    args = get_args()
    configs = load_yml("config")

    the_D = toggl_function.retrieve_toggl_data(CREDENTIALS["toggl"], args.pdf)
    analysis = analyze.analyze_data(the_D)
    # email_function.send(analysis["message"], args.pdf, CREDENTIALS["email"])
    # venmo_function(configs["transfer_amount"], CREDENTIALS["venmo"])

if __name__ == "__main__":
    main()
