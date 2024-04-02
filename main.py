import abc


# Your example application interacts with two different Machines A and B
# that both collect some measurement data.
# The data handling and access of these machines is implementd via the
# two classes DataMachineA and DataMachineB.
#
# Apply the Adapter pattern to the given example, so that
# your application has a uniform access to any current
# and potential future machine. The DataMachineA and DataMachineB classes
# shall stay as they are.
# The adapter shall have a function 'retrieve(index)'
# that shall return a tuple consisting of the type, value and duration
# of a measurement i.

# A class that stores and handles access to some machine of type A
import abc

# A class that stores and handles access to some machine of type A
class DataMachineA:
    def __init__(self):
        # some dummy data
        self.data = {"type": ["A", "A", "B", "B"],
                     "value": [1, 2, 3, 4],
                     "description": ["text1", "text2", "text2", "text3"],
                     "duration": [5, 6, 7, 8]}

    def get_data(self, i):
        return self.data["duration"][i], self.data["type"][i], self.data["value"][i]


# A class that stores and handles access to some machine of type B
class DataMachineB:
    def __init__(self):
        # some dummy data
        self.data = {"type": ["D", "C", "D", "C"],
                     "measurement": [10, 20, 30, 40],
                     "time": [50, 60, 70, 80]}

    def fetch(self, i):
        return self.data["time"][i], self.data["measurement"][i], self.data["type"][i]

# Adapter class to adapt DataMachineB to the interface of DataMachineA
class Adapter(DataMachineB):

    #def __init__(self):
        #self.machine_b=DataMachineB()

    def retrieve(self, i):
       type, value, duration = self.fetch(i)
       return type, value, duration

if __name__ == "__main__":
    dmb = DataMachineB()
    dma = DataMachineA()
    adapter = Adapter()
    print(f"Machine B: {adapter.retrieve(2)}")


