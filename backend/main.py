from tickets import get_loc, get_ticket
import pprint


def main() -> None:
    prompt = input("Please give me a city: ")
    result = get_loc(prompt)
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(result)


if __name__ == "__main__":
    main()
