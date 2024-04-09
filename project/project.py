import requests


def main():
    response = requests.get("https://aax-eu.amazon-adsystem.com/x/c/RMr0Vz6yP3TH_6FyXihShw4AAAGOw-0CYgMAAADKAQBvbm9fdHhuX2JpZDEgICBvbm9fdHhuX2ltcDEgICBAAk9U/https://www.primevideo.com/detail/amzn1.dv.gti.4b0528be-682a-47fa-8016-f3002f05bfc2/?ref_=dvm_crs_imd_in_s_teribaaton")
    reader = response.json()
    print(reader)
def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
