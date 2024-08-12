-- Keep a log of any SQL queries you execute as you solve the mystery.

/* Starting from the crime scene reports table */
SELECT *
FROM crime_scene_reports
WHERE day=28
AND month=7
AND year=2023
AND street="Humphrey Street";
