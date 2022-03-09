import sqlite3 as s
connection = s.connect("Mobile.db")

listoftables = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table ' AND name='SMARTPHONES'").fetchall()

if listoftables != []:
    print("Table already exist")
else:
    connection.execute(''' CREATE TABLE SMARTPHONES(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    SERIAL_NUMBER INTEGER,
                    MODEL_NAME TEXT,
                    BRAND TEXT,
                    MANUFACTURE_YEAR INTEGER,
                    MANUFACTURE_MONTH TEXT,
                    PRICE INTEGER


    ) ''')
    print("Table created Successfully")

while True:
    print("Select an option from menu")
    print("1.Add a Smart Phone ")
    print("2.View all Smart Phones ")
    print("3.Search a Smart Phone using Serial Number ")
    print("4.Update a Smart Phone using Serial Number ")
    print("5.Delete a Smart Phone using Serial Number ")
    print("6.Exit ")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        getSno = input("Enter Serial Number: ")
        getMname = input("Enter Model Name: ")
        getBrand = input("Enter Brand: ")
        getManuyear = input("Enter Manufacture Year: ")
        getManumonth = input("Enter Manufacture Month: ")
        getPrice = input("Enter Price: ")

        connection.execute(" INSERT INTO SMARTPHONES(SERIAL_NUMBER, MODEL_NAME, BRAND, MANUFACTURE_YEAR, \
        MANUFACTURE_MONTH, PRICE) VALUES(" + getSno + ",'" + getMname + "','" + getBrand + "'," + getManuyear + ",\
        '" + getManumonth + "'," + getPrice + ")")
        connection.commit()
        print("Inserted Successfully")

    elif choice == 2:
        result = connection.execute("SELECT * FROM SMARTPHONES")

        for i in result:
            print("Id: ", i[0])
            print("Serial Number: ", i[1])
            print("Model Name: ", i[2])
            print("Brand: ", i[3])
            print("Manufacture Year: ", i[4])
            print("Manufacture Month: ", i[5])
            print("Price: ", i[6])

    elif choice == 3:
        getSno = input("Enter Serial number: ")

        result = connection.execute("SELECT * FROM SMARTPHONES WHERE SERIAL_NUMBER="+getSno)

        for i in result:
            print("Id: ", i[0])
            print("Serial Number: ", i[1])
            print("Model Name: ", i[2])
            print("Brand: ", i[3])
            print("Manufacture Year: ", i[4])
            print("Manufacture Month: ", i[5])
            print("Price: ", i[6])

    elif choice == 4:
        getSno = input("Enter Serial number: ")

        getNsno = input("Enter New Serial Number: ")
        getNmname = input("Enter New Model Name: ")
        getNbrand = input("Enter New Brand: ")
        getNmanuyear = input("Enter New Manufacture Year: ")
        getNmanumonth = input("Enter New Manufacture Month: ")
        getNprice = input("Enter New Price: ")

        result = connection.execute(" UPDATE SMARTPHONES SET SERIAL_NUMBER=" + getNsno + ", MODEL_NAME='" + getNmname + "', \
        BRAND='" + getNbrand + "', MANUFACTURE_YEAR=" + getNmanuyear + ", MANUFACTURE_MONTH='" + getNmanumonth + "',\
        PRICE=" + getNprice + " WHERE SERIAL_NUMBER=" + getSno)
        connection.commit()
        print("Updated Successfully")

    elif choice == 5:
        getSno = input("Enter Serial number: ")

        result = connection.execute("DELETE FROM SMARTPHONES WHERE SERIAL_NUMBER=" + getSno)
        connection.commit()
        print("Deleted Successfully")

    elif choice == 6:
        connection.close()
        break

    else:
        print("Invalid Option")
