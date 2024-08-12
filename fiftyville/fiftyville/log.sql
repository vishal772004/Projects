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

