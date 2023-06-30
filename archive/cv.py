import lorem

WHITE = "\033[1;37m"
NC = "\033[0m"
BULLET = "\u2022"
TAB = " " * 4

# An Experience needs to have:
# - A Title: What I did, this comes first
# - An organization: Where I did it
# - A time period: when I did it
# - a description: Text description of what I did
# - Main Points:
#   - An array of main things I achieved/learned


def right(str_to_format):
    align_len = 115 - len(str_to_format)
    return f"{str_to_format:>{align_len}}"


def left(str_to_format):
    return str_to_format


def left_right(left_str, right_str):
    align_len = 115 - len(left_str) - len(right_str)
    return f"{left_str} {right_str:>{align_len}}"


corti = f"""Data Scientist - Corti.ai {'August 2021 - Present':>81}
    {lorem.sentence()}
    {BULLET} Did work well
    - Did good work with lots of good things
    """

profile = f"{TAB}Profile"
buzzz = f"{WHITE}{'AI MACHINE LEARNING '*5}{NC}"
line = f"{NC}{'_'*115}"
work_experience = f"{TAB}Work Experience"

print(buzzz)
print(profile)
print(line)
print(buzzz)
print(lorem.paragraph())
print(buzzz)
print(buzzz)
print(work_experience)
print(line)
print(corti)
print(left("This is left formatted"))
print(right("This is right formatted"))
print(left_right("this is left", "This is right formatted"))
