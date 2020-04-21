print(range(5)) # Shows the Range Start and Stop values (zero-based) -> range(0, 5)

print (list(range(5))) # Feeding the output from "range" to "list" produces a list -> [0, 1, 2, 3, 4]

print(list(range(5,10))) # Adjusting the START and STOP values for range -> [5, 6, 7, 8, 9]

print(list(range(57,100,2))) # Adjusting the START and STOP values for range  and including the STEP value -> [57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

print(list(range(57,100,-2))) # (STEPPING DOWN FROM LOW TO HIGHER NUMBER) Adjusting the START and STOP values for range  and including the NEGATIVE STEP value -> []
print(list(range(100,57,-2))) # (STEPPING DOWN FROM HIGHER TO LOWER NUMBER) Adjusting the START and STOP values for range  and including the NEGATIVE STEP value -> [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58]

word = "bottles"
for beer_num in range (99,0,-1):
    print(beer_num, word, " of beer on the wall.")
    print(beer_num, word), " of beer."
    print("Take one down...")
    print("Pass it around....")
    if beer_num == 1:
        print('No more bottles of beer on the wall.')
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, " of beer on the wall.")
    print()


print(help(range))