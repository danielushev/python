import os

with open('/home/daniel/Desktop/bundles/results.txt', 'r') as reader:
     # Read and print the entire file line by line
     for line in reader.readlines():
          line2 = line.replace(".", "")
          url = f"/home/daniel/Desktop/bundles/{line2}"
          answer = input(f"Do you want to perform rm -r {url} (Y/N): ")
          if answer == "Y":
            os.system('rm -r ' + url)
            print(f"You deleted {url}")
          elif answer == "N":
            print("You exited the script")  
            exit(1)
