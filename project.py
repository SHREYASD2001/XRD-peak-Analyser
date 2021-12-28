import math

# For structure calculation

def crystal():
    print("Please put the values of (h,k,l) of each first 7 peaks :")

    all_planes_mi = []
    no_of_mi = 7

    # lst1 = []  # square of mi
    lst2 = []  # sum of squares of mi

    for i in range(0, no_of_mi):
        plane = []

        h = int(input("Enter the value of h : "))
        plane.append(h)

        k = int(input("Enter the value of k : "))
        plane.append(k)

        l = int(input("Enter the value of l : "))
        plane.append(l)
        # lst1.append([h * h, k * k, l * l])

        
        all_planes_mi.append(plane)
        lst2.append(h * h + k * k + l * l)

    print("Your planes are ", all_planes_mi)
    print(lst2)


    if lst2 == [1, 2, 3, 4, 5, 6, 8]:
        print("Your sample is having Simple Cubic Structure. ")

    elif lst2 == [2, 4, 6, 8, 10, 12, 14]:
        print("Your sample is having BCC structure. ")

    elif lst2 == [3, 4, 8, 11, 12, 16, 19]:
        print("Your sample is having FCC structure. ")

    elif lst2 == [3, 8, 11, 16, 19, 24, 27]:
        print("Your sample is having DC structure. ")

    else:
        print("Please give right miller indices. ")


def check_peaks():
    a = float(input("Enter the Lattice parameter of the crystal (in A° ) : "))
    w = float(input("Enter the wavelength of X ray (in A° ) : "))
    h_ = int(input("Please put the value of h from the peak's Miller indices : "))
    k_ = int(input("Please put the value of k from the peak's Miller indices: "))
    l_ = int(input("Please put the value of l from the peak's Miller indices : "))

    if (h_*h_) + (k_ * k_) + (l_ * l_) <= (4*(a / w) * (a / w)):
        print("Yes, peak will be shown in XRD pattern. ")

    else:
        print("No, peak will NOT be shown in XRD pattern. ")


print("Hello ! This is an XRD peak analyzer in which following facilities you can get : \n\n(a) Determination of Crystal Structure by giving the input of first 7 (h,k,l) values\n\n(b) Check whether your (h,k,l) peak will be shown in XRD pattern or NOT\n\n")

option = input("Please select any option : ")

if option == 'a' or option == 'A':
    crystal()

elif option == "b" or option == "B":
    check_peaks()