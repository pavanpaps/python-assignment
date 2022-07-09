import datetime

class DateTime:
    def changedate(self):
        curr_date = input("Enter the date: (in DD/MM/YYYY) ")
        new_date = datetime.datetime.strptime(curr_date, "%d/%m/%Y").date()
        print("Date in dd-mm-yyyy format: " + new_date.strftime("%d-%m-%Y"))

def main():
    d = DateTime()
    d.changedate()

if __name__ == "__main__":
    main()