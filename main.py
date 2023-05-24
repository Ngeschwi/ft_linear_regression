
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
        temptheta0 += (price - datasetlist[i][1])
        temptheta1 += (price - datasetlist[i][1]) / datasetlist[i][0]

        temptheta0 = (learningrate / m) * temptheta0
        temptheta1 = (learningrate / m) * temptheta1

        theta0 = temptheta0
        theta1 = temptheta1

    return theta0, theta1

theta0val = 0
theta1val = 0


for i in range(100):
    theta0val, theta1val = descentGradient(theta0val, theta1val)
    print(theta0val, theta1val)

print(estimePrice(theta0val, theta1val, 1000))
