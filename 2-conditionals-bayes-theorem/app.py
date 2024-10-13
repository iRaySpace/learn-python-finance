
# Challenge #1: Spam Filter
# -------------------------
# Suppose 20% of all emails are spam.
# A spam filter is 95% effective at identifying spam (i.e., it correctly identifies 95% of spam emails).
# However, it also incorrectly classifies 10% of non-spam emails as spam (false positives).
# If an email is classified as spam by the filter, what is the probability that it is actually spam?
def _spam_filter():
    # ES => Event where all emails are spam
    p_es = 0.20

    # FS => Event where emails are filtered as spams
    # P(FS | ES) -> Probability of emails filtered as spam given that emails are spam
    # P(FS | not ES) -> PRobability of emails filtered as spam given that emails are not spam
    p_fs_es = 0.95
    p_fs_not_es = 0.10

    # What is the probability that emails are actually spam after filtered as spam?
    # P(ES | FS) -> Probability that emails are SPAM after filtered as spam
    # P(ES | FS) = P(ES ∩ FS) / P(FS)
    # P(ES | FS) = P(ES) * P(FS | ES) / P(FS)
    # Given: P(ES), P(FS | ES)
    # Missing: P(FS)
    # P(FS) = ∑ (Probability of events that ∩ with FS)
    # P(FS) = P(ES ∩ FS) + P(not ES ∩ FS)
    # P(FS) = ( P(ES) * P(FS|ES) ) + ( P(not ES) * P (FS|not ES) )
    p_not_es = 1.0 - p_es
    print("P(not ES):", p_not_es)

    p_fs = (p_es * p_fs_es) + (p_not_es * p_fs_not_es)
    print("P(FS):", p_fs)

    # Computing after getting other probabilities
    p_es_fs = (p_es * p_fs_es) / p_fs
    print("P(ES | FS):", p_es_fs)


# Challenge #2: Quality Control in a Factory
# -----------------------------------------
# A factory produces 80% of its products from Machine A and 20% from Machine B. 
# Machine A has a defect rate of 2%, while Machine B has a defect rate of 5%. 
# If a randomly selected product is found to be defective, what is the probability that it was produced by Machine B?
def _quality_control():
    # A => Event where it was produced from Machine A
    p_a = 0.8

    # B => Event where it was produced from Machine B
    p_b = 0.2

    # D => Event where it's defect
    # P(D | A) => Defect rate of the products from A
    # P(D | B) => Defect rate of the products from B
    p_d_a = 0.02
    p_d_b = 0.05

    # If a randomly selected product is found to be defective, what is the probability produced by Machine B?
    # P(B | D) = ?
    # P(B | D) = P(B ∩ D) / P(D)
    # P(B | D) = (P(B) * P(D | B)) / P(D)
    # P(D) = ?
    # P(D) = ∑ (Probability of events that ∩ with D)
    # P(D) = P(A ∩ D) + P(B ∩ D)
    # P(D) = P(A) * P(D | A) + P(B) * P(D | A)
    p_d = (p_a * p_d_a) + (p_b * p_d_b)
    print("P(D):", p_d)
    
    p_b_d = (p_b * p_d_b) / p_d
    print("P(B | D):", p_b_d)


def _main():
    print("""
# Challenge #1: Spam Filter
# -------------------------
# Suppose 20% of all emails are spam.
# A spam filter is 95% effective at identifying spam (i.e., it correctly identifies 95% of spam emails).
# However, it also incorrectly classifies 10% of non-spam emails as spam (false positives).
# If an email is classified as spam by the filter, what is the probability that it is actually spam?
    """)
    _spam_filter()

    print("""
# Challenge #2: Quality Control in a Factory
# -----------------------------------------
# A factory produces 80% of its products from Machine A and 20% from Machine B. 
# Machine A has a defect rate of 2%, while Machine B has a defect rate of 5%. 
# If a randomly selected product is found to be defective, what is the probability that it was produced by Machine B?
    """)
    _quality_control()


if __name__ == '__main__':
    _main()
