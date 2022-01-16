with open('travels.txt', 'r') as f:
    for i in f:
        l = i.split()
        october_1 = 0
        october_2 = 0
        october_3 = 0

        m_lipky = 0

        sum_rast = 0

        punkt_names = []

        if l[0] == 1:
            october_1 += l[6]
        elif l[0] == 2:
            october_2 += l[6]
        elif l[0] == 3:
            october_3 += l[6]


        if l[2] == 'Липки':
            m_lipky += l[0]


        if l[0] == 1:
            sum_rast += l[4]