
data = open('data.csv', 'r')
dataread = data.read()
dataset = dataread.split('\n')[1:]
datasetlist = [i.split(',') for i in dataset]
m = len(datasetlist)
for i in range(m):
    datasetlist[i][0] = int(datasetlist[i][0])
    datasetlist[i][1] = int(datasetlist[i][1])
data.close()

learningrate = 0.1

def estimePrice(theta0, theta1, mileage):
    price = theta0 + theta1 * mileage
    return price


def descentGradient(theta0, theta1):
    temptheta0 = theta0
    temptheta1 = theta1

    for i in range(m):
        price = estimePrice(theta0, theta1, datasetlist[i][0])
        temptheta0 = temptheta0 - (learningrate*(price-datasetlist[i][1])) / m

    theta0 = temptheta0

    for i in range(m):
        price = estimePrice(theta0, theta1, datasetlist[i][0])
        temptheta1 = temptheta1 + (learningrate * (price-datasetlist[i][1]) / datasetlist[i][0]) / m

    theta1 = temptheta1

    return theta0, theta1

theta0val = 0
theta1val = 0


for i in range(10000):
    theta0val, theta1val = descentGradient(theta0val, theta1val)
    print(theta0val, theta1val)

print(estimePrice(theta0val, theta1val, 1000))

import matplotlib.pyplot as plt

x = [datasetlist[i][0] for i in range(m)]
y = [datasetlist[i][1] for i in range(m)]

plt.scatter(x , y)

y = [theta0val + theta1val*i for i in x]

plt.plot(x , y , color = 'r')

plt.show()
