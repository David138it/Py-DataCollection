#import sys  # sys нужен для передачи argv в QApplication
#from PyQt5 import QtWidgets
#import design  # Это наш конвертированный файл дизайна
#class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
#    def __init__(self):
#        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
#        super().__init__()
#        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

#def main():
#    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#    window = ExampleApp()  # Создаём объект класса ExampleApp
#    window.show()  # Показываем окно
#    app.exec_()  # и запускаем приложение
#if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#    main()  # то запускаем функцию main()
def replData(ip1, ip2, sName, sNumb, tNumb):
    # список ключей, которые нужно будет заменить в файле template
    keys=['_ip1_', '_ip2_', '_sName_', '_sNumb_', '_tNumb_']
    #print(keys) 
    #print(keys[2])
    #Создаем список значений, на которые нужно будет заменить
    values=[]
    values.append(ip1)
    values.append(ip2)
    values.append(sName)
    values.append(sNumb)
    values.append(tNumb)
    #print(values)
    #print(values[2])
    #Создаем словарь. в качестве ключей (keys) это будут список значений, в 
        #котором надо будет заменить в файле template, а в качестве значений 
        #(values) - список значений, на которые нужно будет заменить
    dictionary={}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
        search_text = dictionary[keys[i]]
        replace_text = keys[i]
        #print(search_text)
        #print(replace_text)
    #Считываем файл template, и меняем значения
    with open(r'template.txt', 'r') as oFile:
        rFile = oFile.read()
        for key, value in dictionary.items():
            rFile = rFile.replace(key, str(value))
    #print(rFile)    
    #Запишем изменения в файл output
    with open(r'output.txt', 'a') as wFile:
        wFile.write('\n')
        wFile.write('\n')
        wFile.write('\n')
        wFile.write(rFile)    
repeat="y"
while repeat == "y":
    #ip1, ip2, sName, sNumb, tNumb = 1111, 2222, 3333, 4444, 5555
    ip1, ip2, sName, sNumb, tNumb = input("Enter the IP address1: "), input("Enter the IP address2: "), input("Enter the station name: "), input("Enter the station number: "), input("Enter the transmitter number: ")    
    replData(ip1, ip2, sName, sNumb, tNumb)
    #Если нужно повторить:
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
    while (repeat!="y" and repeat!="n"):
        repeat = input("Please enter the correct answer (y/n): ")