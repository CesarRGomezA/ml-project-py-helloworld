import matplotlib.pyplot as plt 

years = [1950, 1970, 1990, 2010]

population = [2.519, 3.692, 5.263, 6.972]

deaths = [2.239, 5.692, 2.263, 2.972]

plt.title('Poblacion anual')

plt.xlabel('años')
plt.ylabel('poblacion')


plt.plot(years, population, 'r')
plt.plot(years, deaths, 'pink' )
plt.scatter(years, population, color = 'green')
plt.scatter(years, deaths, color = 'orange')
plt.legend(['crecimiento', 'muertes'])

plt.show()