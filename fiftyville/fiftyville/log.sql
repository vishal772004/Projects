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

/*Then after careful observation we head on to the baker_security_logs*/
SELECT *
FROM bakery_security_logs
WHERE year=2023
AND month=7
AND day=28
AND hour=10
AND minute>15
and activity="exit";

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
AND atm_location="Leggett Street"
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
WHERE a.year=2023
AND a.month=7
AND a.day=28
AND a.atm_location="Leggett Street"
AND a.transaction_type="withdraw"
AND p.phone_number
IN(
    SELECT caller
    FROM phone_calls
    WHERE year=2023
    AND month=7
    AND day=28
    and duration<60
);

/*Now we try to find the thief who stole the duck by analyzing the withdrawal ,call history and checking the licence plate at the bakery*/

SELECT distinct(p.name)
FROM bank_accounts
AS b
JOIN atm_transactions
AS a
ON b.account_number=a.account_number
JOIN people
AS p
ON p.id=b.person_id
JOIN phone_calls
AS ph
ON ph.caller=p.phone_number
WHERE a.year=2023
AND a.month=7
AND a.day=28
AND a.atm_location="Leggett Street"
AND a.transaction_type="withdraw"
AND ph.caller
IN(
    SELECT caller
    FROM phone_calls
    WHERE year=2023
    AND month=7
    AND day=28
    and duration<60
)
AND p.license_plate
IN(
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year=2023
    AND month=7
    AND day=28
    AND hour=10
    AND minute<25
    AND minute>15
    AND activity="exit"
);
/* Now we try to find the person who booked a flight*/
SELECT name
FROM people
WHERE passport_number
IN(
    SELECT DISTINCT(passport_number)
    FROM passengers,flights
    WHERE flight_id
    IN(
        SELECT id
        FROM flights
        WHERE day=29
        AND month=7
        AND year=2023
        AND origin_airport_id=(
            SELECT id
            FROM airports
            WHERE city="Fiftyvile"
        )
        ORDER BY hour
    )
)
AND phone_number
IN(
    SELECT receiver
    FROM phone_calls
    WHERE day=29
    AND month=7
    AND year=2023
    AND duration<60
);

