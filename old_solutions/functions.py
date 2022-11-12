values = []
with open("input.txt") as f:
    # for line in f:
    # print(line.strip())
    values = f.readline().split()
print(values)

services, features = [], []
line_numbers = [i for i in range(1, int(values[2]) + 1)]
line_numbers_2 = [
    i for i in range(int(values[2]) + 1, int(values[2]) + 2 * int(values[5]) + 1)
]

with open("input.txt") as f:
    for i, line in enumerate(f):
        if i in line_numbers:
            services.append(line.strip().split())
        elif i > int(values[2]):
            break
print(services)

binaries = [[] for i in range(len(services))]
for i in range(0, len(services)):
    binaries[int(services[i][1])].append(services[i][0])
print(binaries)
newBinaries = [[] for i in range(len(services))]
for i in range(0, len(services)):
    newBinaries[int(services[i][1])].append(services[i][0])
newBinary = [[] for i in range(len(services))]
for i in range(0, len(services)):
    newBinary[int(services[i][1])].append(services[i][0])

with open("input.txt") as f:
    for i, line in enumerate(f):
        if i in line_numbers_2:
            features.append(line.strip().split())
        elif i > int(int(values[2]) + 2 * int(values[5])):
            break
NewFeatures = []
for k in range(0, len(features) // 2):
    NewFeatures.append(features[2 * k] + features[2 * k + 1])
NewFeatures.sort(key=lambda inner_list: int(inner_list[3]), reverse=True)
print(NewFeatures)


def indices(lst, element):
    for count, val in enumerate(lst):
        if element in val:
            return count


def impl_cost(F: str, val: list, binary: list):
    bin = []
    count = 0
    for k, values in enumerate(val):
        if values[0] == F:
            services = values[4:]
            break
    for service in services:
        if indices(binary, service) not in bin:
            bin.append(indices(binary, service))
    for i in bin:
        count = count + len(binary[i])
    return count + len(bin) * int(val[k][2])


# print(impl_cost('foo', NewFeatures, binaries))


def move_cost(F: str, val: list, binary: list):
    bin = []
    for k, values in enumerate(val):
        if values[0] == F:
            services = values[4:]
            break
    for service in services:
        if indices(binary, service) not in bin:
            bin.append(indices(binary, service))
    return max(len(binary[bin[0]]), len(binary[bin[0]]))


def feature_in_one_bin(F: str, val: list, binary: list):
    bin = []
    for k, values in enumerate(val):
        if values[0] == F:
            services = values[4:]
            break
    for service in services:
        if indices(binary, service) not in bin:
            bin.append(indices(binary, service))
    if len(bin) == 1:
        return True
    return False


print(move_cost("foo", NewFeatures, binaries))


def moving_service(binary, source, target, S):
    i = binary[source].pop(binary[source].index(S))
    binary[target].append(i)
    return binary


newBinaries = moving_service(newBinaries, 1, 2, "sc")


print(
    impl_cost("foo", NewFeatures, newBinaries) + move_cost("foo", NewFeatures, binaries)
)


def mk_new_bin(bin):
    return bin.append([])


print(int(values[5]))
