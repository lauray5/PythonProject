def generate_testcase_id():
    for i in range(1, 10000):
        case_id = 'C' + str(i).zfill(2) + '_'
        yield case_id

m_id = generate_testcase_id()
c_id = generate_testcase_id()
