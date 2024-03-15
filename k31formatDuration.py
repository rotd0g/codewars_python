def format_duration(seconds):
    """
    Our task in order to complete this Kata is to write a function which formats a duration,
    given as a number of seconds, in a human-friendly way.

    The function must accept a non-negative integer. If it is zero, it just returns "now".
     Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

    It is much easier to understand with an example:

    * For seconds = 62, your function should return
        "1 minute and 2 seconds"
    * For seconds = 3662, your function should return
        "1 hour, 1 minute and 2 seconds"
    For the purpose of this Kata, a year is 365 days and a day is 24 hours.

    Note that spaces are important.
    """
    duration = []

    if seconds == 0:
        return 'now'

    # YEARS
    years = seconds // (365 * 24 * 60 * 60)
    if years > 0:
        duration.append(f'{years} year{"s" if years > 1 else""}')
    # elif years > 1:
    #     duration.append(f'{years} years')
    # print(duration)

    seconds -= years * (365 * 24 * 60 * 60)
    # YEARS print(seconds)

    # DAYS
    days = seconds // (24 * 60 * 60)
    if days > 0:
        duration.append(f'{days} day{"s" if days > 1 else ""}')
    # print(duration)

    seconds -= days * (24 * 60 * 60)
    # print(seconds)

    #HOURS
    hours = seconds // (60 * 60)
    if hours > 0:
        duration.append(f'{hours} hour{"s" if hours > 1 else ""}')
    # print(duration)

    seconds -= hours * (60 * 60)
    # print(seconds)


    #MIN
    minutes = seconds // ( 60)
    if minutes > 0:
        duration.append(f'{minutes} minute{"s" if minutes > 1 else ""}')
    # print(duration)

    seconds -= minutes * (60)

    #SEC
    if seconds > 0:
        duration.append(f'{seconds} second{"s" if seconds > 1 else ""}')

    # print(duration)

    return ', '.join(duration[:-1]) + f' and {duration[-1]}' if len(duration) > 1 else duration[0]

print(format_duration(361202))
