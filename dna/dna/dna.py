import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv)!=3):
        sys.exit(1)

    # TODO: Read database file into a variable
    l1 = []
    with open(sys.argv[1]) as file:
        dreader = csv.DictReader(file)
        for i in dreader:
            l1.append(dreader.fieldnames)
    ssub = []
    for i in l1:
        for j in i:
            if j=="name":
                continue
            ssub.append(j)

    # TODO: Read DNA sequence file into a variable
    l2 = []
    with open(sys.argv[2]) as file:
        sreader = csv.DictReader(file)
        l2.append(sreader.fieldnames)
    s = l2[0][0]

    # TODO: Find longest match of each STR in DNA sequence
    d = dict()
    for i in ssub:
        longest_run = longest_match(s,i)
        d[i] = longest_run
    # TODO: Check database for matching profiles
    with open(sys.argv[1]) as file:
        dreader = csv.DictReader(file)
        for i in dreader:
            print(i)
        for i in d:
            print(i)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
