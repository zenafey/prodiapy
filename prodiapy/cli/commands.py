import getpass
import keyring


def login_parser(command_parser) -> None:
    login_parser = command_parser.add_parser(
        "login", help="Login Prodia API."
    )
    login_parser.set_defaults(func=_login)

    login_parser.add_argument(
        "token",
        help="API token",
    )


def _login(namespace):
    token = getattr(namespace, "token", None)

    if token is None:
        token = getpass.getpass("Enter your API token: ")

    keyring.set_password("prodiapy", "bob", token)
    print("Your token was securely stored")

