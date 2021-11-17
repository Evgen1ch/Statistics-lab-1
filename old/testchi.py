# d = Distribution(pd.read_csv("data_lab1/500/veib.txt", header=None))
    # x = d.population_['x']
    # y = d.population_['cumulative-probability']

    # a, b, cia, cib, = restore_veibull_distribution(x[:-1], y[:-1])
    # print(a, b)

    # xi = np.linspace(x.min(), x.max(), 1000)
    # ci = weib(x, a, b)
    # dens = weib_density(x, a, b)

    # plt.figure(figsize=(10, 10), dpi=150)

    # plt.plot(x, ci, c='orange',
    #          label='restored 1.0 - exp(-x^b/a)\na = {0}\nb = {1}'.format(a, b))

    # plt.scatter(x, y, s=3)
    # plt.legend()

    # fig, ax = plt.subplots(dpi=150)
    # ax.plot(x, dens, c='green')
    # x.plot(kind='density', bw_method=.25)
    # ax.hist(x, density=True, alpha=0.5)
    # plt.show()

    # x = d.population_['x'].values
    # probable, chi2, crit = chi_square_test(x, a, b, 0.05, 200)
    # print(probable, chi2, crit)