import yaml
import argparse


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
