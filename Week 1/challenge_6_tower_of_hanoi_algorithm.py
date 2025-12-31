

def towerOfHanoi(N, from_rod, aux_rod, to_rod):
    '''
    The function acts as the tower of Hanoi. It follows the rule that we move function N - 1 disks from rod 1,
    then 1 disk from rod 2 and then N - 1 from rod 3.
    It prints each move along thr way it moves to the end.
    
    :param N: The number of disks
    :param from_rod: Rod containing initially all disks
    :param aux_rod: To help moving the disks
    :param to_rod: The rod that should get the correct order
    '''
    
    if N < 0:   # Exception case
        print("Invalid number of disks provided")
        return
    
    if N == 1:  # If the disk left if 1
        print(f"Disk 1 moved from {from_rod} to {to_rod}")
        return
    
    towerOfHanoi(N-1, from_rod, to_rod, aux_rod)        
    
    print(f"Disk {N} moved from {from_rod} to {to_rod}")

    towerOfHanoi(N-1, aux_rod, from_rod, to_rod)

disks = 4
print("Disks:", disks)
from_rod = "A"
aux_rod = "B"
to_rod = "C"
print(f"To rod: {to_rod}, Aux rod: {aux_rod}, From rod: {from_rod}")
print("Steps:")
towerOfHanoi(disks, from_rod, aux_rod, to_rod)
