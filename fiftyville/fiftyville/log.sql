-- Keep a log of any SQL queries you execute as you solve the mystery.

/* Starting from the crime scene reports table with the available information */
SELECT *
FROM crime_scene_reports
WHERE day=28
AND month=7
AND year=2023
AND street="Humphrey Street";

/*After observing the description then we head on to the interviews table*/
SELECT *
FROM interviews
WHERE year=2023
AND month=7
AND day=28;

/*Then after careful observation we head on to the bakery security footage */
SELECT *
FROM interviews
WHERE year=2023
AND month=7
AND day=28
AND hour=10
AND minute>15;

/*Having the list of licence plates we next move to the atm transactions as told by the witness*/
SELECT *
FROM atm_transactions
WHERE year=2023
AND month=7
AND day=28
AND atm_location="Leggitt Street"
AND transaction_type="withdraw";

/*Having the list of account number we then move on to the bank accounts table to have the list of names who  withdraw their money*/
SELECT p.name
FROM bank_accounts
AS b
JOIN atm_transactions
AS a
ON b.account_number=a.account_number
JOIN people
AS p
ON p.id=b.person_id
WHERE year=2023
AND month=7
AND day=28
AND atm_location="Leggitt Street"
AND transaction_type="withdraw";

/*Now we try to shortlist the names of people who withdrew their money and spoke to someone on call for less than a minute*/

SELECT p.name,p.phone_number
FROM bank_accounts
AS b
JOIN atm_transactions
AS a
ON b.account_number=a.account_number
JOIN people
AS p
ON p.id=b.person_id
WHERE year=2023
AND month=7
AND day=28
AND atm_location="Leggitt Street"
AND transaction_type="withdraw";
