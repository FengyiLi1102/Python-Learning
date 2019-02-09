def age_reversible(times):
    """
    Find two persons with ages which are able to experience 'times' number of mirror symmetry for their
    digits.
    :param times: number of times
    :return: None
    """
    for m_age in range(99, 1, -1):
        for d_age in range(m_age - 1, 0, -1):
            times_sum = 0
            m_age_record = m_age
            d_age_record = d_age

            while d_age_record > 0:
                m_age_str = str(m_age_record).zfill(2)
                d_age_str = str(d_age_record).zfill(2)
                if m_age_str[1] == d_age_str[0]:
                    times_sum += 1

                m_age_record -= 1
                d_age_record -= 1

            if times_sum == times and d_age_record + 18 < m_age_record:
                times_record = 0
                while d_age_record < d_age:
                    m_age_str = str(m_age_record).zfill(2)
                    d_age_str = str(d_age_record).zfill(2)
                    if m_age_str[1] == d_age_str[0]:
                        times_record += 1
                    if times_record == 6:
                        print(m_age_record, d_age_record, times_record)
                    d_age_record += 1
                    m_age_record += 1

