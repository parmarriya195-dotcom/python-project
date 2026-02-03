li = []
total_count = 0

def add():
    """Accepts comma separated values and stores them in a 1D list"""
    global total_count
    data = input("Enter data for 1D array (comma separated): ")
    numbers = list(map(int, data.split(",")))
    li.extend(numbers)
    total_count = len(li)

def average(data):
    """Calculates average of the list"""
    return sum(data) / len(data)

def facto(n):
    """Calculates factorial using recursion"""
    if n <= 1:
        return 1
    return n * facto(n-1)

def show_values(*args):
    """Displays values using *args"""
    print("Values:", args)

def dataset_stats(**kwargs):
    """Displays dataset statistics using **kwargs"""
    for k, v in kwargs.items():
        print(k, ":", v)

def get_stats(data):
    """Returns multiple values (min, max, sum, average)"""
    return min(data), max(data), sum(data), sum(data) / len(data)

while True:
    print("\nWelcome to the data analyzer and transformer program!\n")

    print("\nMain menu:")
    print("1. Input data")
    print("2. Display data summary")
    print("3. Calculate factorial (recursion)")
    print("4. Filter data by thresold")
    print("5. Sort data")
    print("6. Display dataset stastics (return multiple vlaues)")
    print("7. Exit\n")
   
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        add()
        print("Data has been stored successfully!\n")

    elif choice == 2:
        print("\nData summary:")
        print("Total numbers:", len(li))
        print("Minimum:", min(li))
        print("Maximum:", max(li))
        print("Sum:", sum(li))
        avg = average(li)
        print("Average:", avg)

    elif choice == 3:
        fact = int(input("Enter a number to calculate its factorial: "))
        print("Factorial:", facto(fact))

    elif choice == 4:
        val = int(input("Enter a threshold value: "))
        filtered = list(filter(lambda x: x >= val, li))
        print("Filtered data:", filtered)

    elif choice == 5:
        print("1. Ascending")
        print("2. Descending")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            li.sort()
            print("Sorted list:", li)
        else:
            li.sort(reverse=True)
            print("Sorted list:", li)

    elif choice == 6:
        mn, mx, sm, avg = get_stats(li)

        dataset_stats(
            Minimum=mn,
            Maximum=mx,
            Sum=sm,
            Average=avg
        )
    elif choice == 7:
        print("Thanks for visit!")
        break
 
    else:
        print("Invalid choice!")