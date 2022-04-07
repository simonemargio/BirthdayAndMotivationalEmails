import smtplib
import random
import pandas
import datetime as dt

# You must enter your email and password. Beware that some providers such as Google do not accept the email password,
# but you have to create an application password.
email = "your_email"
password = "your_email_password"


def random_quote():
    """
    Takes a casual quote from Steve Jobs
    :return: string containing the quote
    """
    with open("steve_jobs_quotes.txt", mode="r") as file:
        data = file.read().splitlines()
        quote = random.choice(data)
    return quote


def random_letter_birthday(receiver):
    """
    Generate a random birthday letter
    :param receiver: name of the person celebrating the birthday
    :return: string containing the letter to send
    """
    n_letter = random.randint(1, 3)
    with open(f"letter_birthday_templates/letter_{n_letter}.txt") as file:
        standard_letter = file.read()
        letter = standard_letter.replace('[NAME]', str(receiver))
        return letter


def random_letter_monday_motivation(receiver):
    """
    Generate a random monday monday letter
    :param receiver: name of the person
    :return: string containing the letter to send
    """
    n_letter = random.randint(1, 3)
    with open(f"letter_monday_motivation/letter_{n_letter}.txt") as file:
        standard_letter = file.read()
        letter = standard_letter.replace('[NAME]', str(receiver))
        quote = random_quote()
        letter += "\n\n" + quote
        return letter


def send_email(receiver, smtp, subject, letter):
    """
    Generate a random monday monday letter
    :param receiver: email of receiver
    :param smtp: smtp of email
    :param subject: subject of letter
    :param letter: object of letter
    """
    with smtplib.SMTP(smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver,
            msg=f"Subject:{subject}\n\n{letter}")


def check_email_smtp(email):
    """
    Return the right smtp based on the email
    :param email: email
    :return: smtp of email
    """
    email = email.rpartition('@')[2]
    email = email.rpartition('.')[0]
    match email:
        case "gmail":
            return "smtp.gmail.com"
        case "hotmail":
            return "smtp.live.com"
        case "outlook":
            return "smtp.live.com"
        case "yahoo":
            return "smtp.mail.yahoo.com"
        case "icloud":
            return "smtp.mail.me.com"


# Get the current day and read the file containing the information
current_date_time = dt.datetime.now()
data = pandas.read_csv("receiver_email.csv")

# Single line reading
for (index, row) in data.iterrows():
    name_receiver = row.receiver
    email_receiver = row.email
    smtp = check_email_smtp(email_receiver)

    if smtp:
        # Check of the day Monday
        if current_date_time.weekday() == 0:
            letter = random_letter_monday_motivation(name_receiver)
            send_email(email_receiver, smtp, "Monday motivation :)", letter)

        # Checking the birthday
        if current_date_time.month == row.month and current_date_time.day == row.day:
            letter = random_letter_birthday(name_receiver)
            send_email(email_receiver, smtp, "Hey :)", letter)
