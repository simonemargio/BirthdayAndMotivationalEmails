# Birthday and motivational send

## Index
1. [What is](#what-is)
2. [Dependencies](#dependencies)
3. [Run](#run)



### What is
Send birthday and motivational emails with Python. The greeting and motivational monday emails are randomly chosen from a list of predefined letters in: *"letter_birthday_templates"* and *"letter_monday_motivation"*.  
The Monday letters also contain a casual quote from Steve Jobs.

### Dependencies
Pandas is used to read the CSV file containing the emails to send the letters to.
```
pip3 install pandas
```
### Run
In main.py you have to enter your email and password.  
Update the receiver_email.csv file with all the contacts you want to check.
```
python3 main.py
```
