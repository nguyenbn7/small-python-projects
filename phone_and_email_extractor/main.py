import re

phone_regex_pattern = re.compile(
    r"""(
        (\d{3}|\(\d{3}\))?                  # area code
        (\s|-|\.)?                          # seperator
        (\d{3})                             # first 3 digits
        (\s|-|\.)                           # seperator
        (\d{4})                             # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )""",
    re.VERBOSE,
)
