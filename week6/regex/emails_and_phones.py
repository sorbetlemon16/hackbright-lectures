import re

UBERMELON_EMAIL_RE = re.compile(r"\w+\@ubermelon\.com")
PHONE_RE = re.compile(r"(\d{3})-(\d{3}-\d{4})")

def print_ubermelon_emails(text):
    """Print all the ubermelon emails in the input text."""

    # Loop over all ubermelon email addresses in text
    for email in re.findall(UBERMELON_EMAIL_RE, text):
        print("Found: {}".format(email))


def print_phone_numbers(text):
    """Group phone numbers in the text by area code, and print groups."""

    # dict for grouping phone numbers by area code
    phone_nums = {}

    # because PHONE_RE has groups, re.findall will return a list of tuples
    for area_code, phone_num in re.findall(PHONE_RE, text):
        
        # create a new list value if the area code isn't represented in dict
        if area_code not in phone_nums:
            phone_nums[area_code] = [phone_num]

        # otherwise, add to existing list
        else:
            phone_nums[area_code].append(phone_num)

        
    # print info
    for area_code, nums in phone_nums.items():
        print()
        print("Phone numbers in {}".format(area_code))
        for num in nums:
            print("\t{}".format(num))


if __name__ == '__main__':

    # Read in HTML contact page as a single string
    contact_page = open("contact.html").read()

    print_ubermelon_emails(contact_page)

    print_phone_numbers(contact_page)