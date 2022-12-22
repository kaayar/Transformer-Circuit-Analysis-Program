from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtGui
import sys
import calculation

class Transformer_app(QMainWindow):
    def __init__(self):
        super(Transformer_app, self).__init__()
        self.setGeometry(250, 120, 1300, 900)
        self.setWindowTitle("Transformer_SC_OC_TEST by kshitij vijay(121EE1072)")
        self.initUI()

    def initUI(self):

        self.background_img = QtWidgets.QLabel(self)
        self.background_img.setGeometry(0,0,1300, 900)
        picture = QPixmap("3175.jpg")
        self.background_img.setPixmap(picture)
        self.background_img.move(1, 1)

        self.background_img = QtWidgets.QLabel(self)
        


        self.label_Hoc = QtWidgets.QLabel(self)
        self.label_Hoc.setText("OPEN CIRCUIT TEST")
        self.label_Hoc.move(170, 500)
        self.label_Hoc.setFont(QtGui.QFont('Italic',13))
        self.label_Hoc.resize(330,20)

        self.label_Hsc = QtWidgets.QLabel(self)
        self.label_Hsc.setText("SHORT CIRCUIT TEST")
        self.label_Hsc.move(850, 500)
        self.label_Hsc.setFont(QtGui.QFont('Italic',13))
        self.label_Hsc.resize(350,20)

        self.label_Ioc = QtWidgets.QLabel(self)
        self.label_Ioc.setText("Current: ")
        self.label_Ioc.move(210, 550)
        self.label_Ioc.setFont(QtGui.QFont('Times',10))

        self.label_Voc = QtWidgets.QLabel(self)
        self.label_Voc.setText("Voltage: ")
        self.label_Voc.move(210, 650)
        self.label_Voc.setFont(QtGui.QFont('Times',10))

        self.label_Woc = QtWidgets.QLabel(self)
        self.label_Woc.setText("Power: ")
        self.label_Woc.move(210, 750)
        self.label_Woc.setFont(QtGui.QFont('Times',10))

        self.label_Isc = QtWidgets.QLabel(self)
        self.label_Isc.setText("Current: ")
        self.label_Isc.move(880, 550)
        self.label_Isc.setFont(QtGui.QFont('Times',10))

        self.label_Vsc = QtWidgets.QLabel(self)
        self.label_Vsc.setText("Voltage: ")
        self.label_Vsc.move(880, 650)
        self.label_Vsc.setFont(QtGui.QFont('Times',10))

        self.label_Wsc = QtWidgets.QLabel(self)
        self.label_Wsc.setText("Power: ")
        self.label_Wsc.move(890, 750)
        self.label_Wsc.setFont(QtGui.QFont('Times',10))

        self.label_Iw= QtWidgets.QLabel(self)
        self.label_Iw.setText("Iw: ")
        self.label_Iw.move(950, 40)
        self.label_Iw.setFont(QtGui.QFont('Times',10))
        self.label_Iw.resize(140,20)

        self.label_Im = QtWidgets.QLabel(self)
        self.label_Im.setText("Iμ: ")
        self.label_Im.move(950, 80)
        self.label_Im.setFont(QtGui.QFont('Times',10))
        self.label_Im.resize(140,20)

        self.label_Ro = QtWidgets.QLabel(self)
        self.label_Ro.setText("Ro: ")
        self.label_Ro.move(950, 120)
        self.label_Ro.setFont(QtGui.QFont('Times',10))
        self.label_Ro.resize(140,20)

        self.label_Xo = QtWidgets.QLabel(self)
        self.label_Xo.setText("Xo: ")
        self.label_Xo.move(950, 160)
        self.label_Xo.setFont(QtGui.QFont('Times',10))
        self.label_Xo.resize(140,20)

        self.label_Ro1 = QtWidgets.QLabel(self)
        self.label_Ro1.setText("Ro1: ")
        self.label_Ro1.move(950, 200)
        self.label_Ro1.setFont(QtGui.QFont('Times',10))
        self.label_Ro1.resize(140,20)

        self.label_Xo1 = QtWidgets.QLabel(self)
        self.label_Xo1.setText("Xo1: ")
        self.label_Xo1.move(950, 240)
        self.label_Xo1.setFont(QtGui.QFont('Times',10))
        self.label_Xo1.resize(140,20)

        self.label_pf = QtWidgets.QLabel(self)
        self.label_pf.setText("Cosφ: ")
        self.label_pf.move(950, 280)
        self.label_pf.setFont(QtGui.QFont('Times',10))
        self.label_pf.resize(140,20)


        self.linetext_oi = QtWidgets.QLineEdit(self)
        self.linetext_oi.setPlaceholderText("in Amp")
        self.linetext_oi.move(275, 550)
        self.linetext_oi.setStyleSheet("QLineEdit {  border: 2px solid gray;""border-radius: 5px;}")
        

        self.linetext_ov = QtWidgets.QLineEdit(self)
        self.linetext_ov.setPlaceholderText("in Volt")
        self.linetext_ov.move(275, 650)
        self.linetext_ov.setStyleSheet("QLineEdit {  border: 2px solid gray;""border-radius: 5px;}")


        self.linetext_ow = QtWidgets.QLineEdit(self)
        self.linetext_ow.setPlaceholderText("in Watt")
        self.linetext_ow.move(275, 750)
        self.linetext_ow.setStyleSheet("QLineEdit {  border: 2px solid gray;""border-radius: 5px;}")


        self.linetext_si = QtWidgets.QLineEdit(self)
        self.linetext_si.setPlaceholderText("in Amp")
        self.linetext_si.move(950, 550)
        self.linetext_si.setStyleSheet("QLineEdit {  border: 2px solid gray;""border-radius: 5px;}")

        self.linetext_sv = QtWidgets.QLineEdit(self)
        self.linetext_sv.setPlaceholderText("in Volt")
        self.linetext_sv.move(950, 650)
        self.linetext_sv.setStyleSheet("QLineEdit {  border: 2px solid gray;""border-radius: 5px;}")


        self.linetext_sw = QtWidgets.QLineEdit(self)
        self.linetext_sw.setPlaceholderText("in W")
        self.linetext_sw.move(950, 750)
        self.linetext_sw.setStyleSheet("QLineEdit {  border: 2px solid gray;""border-radius: 5px;}")


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Calculate")
        self.b1.move(600, 800)
        self.b1.clicked.connect(self.clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Clear")
        self.b2.move(600, 850)
        self.b2.clicked.connect(self.clickme)

        self.diagram_Iw = QtWidgets.QLabel(self)
        
        self.diagram_Im = QtWidgets.QLabel(self)
        
        self.diagram_Xo = QtWidgets.QLabel(self)
        
        self.diagram_Ro = QtWidgets.QLabel(self)
        
        self.diagram_Ro1 = QtWidgets.QLabel(self)
        
        self.diagram_Xo1 = QtWidgets.QLabel(self)
        

    def clicked(self):       
        oi = self.linetext_oi.text()
        oi_user_input = float(oi)
        a = oi_user_input 

        ov = self.linetext_ov.text()
        ov_user_input = float(ov)
        b = ov_user_input

        ow = self.linetext_ow.text()
        ow_user_input = float(ow)
        c = ow_user_input

        si = self.linetext_si.text()
        si_user_input = float(si)
        d = si_user_input

        sv = self.linetext_sv.text()
        sv_user_input = float(sv)
        e = sv_user_input

        sw = self.linetext_sw.text()
        sw_user_input = float(sw)
        f = sw_user_input

        calculation.values[0] = a
        calculation.values[1] = b
        calculation.values[2] = c
        calculation.values[3] = d
        calculation.values[4] = e
        calculation.values[5] = f
        calculation.oi = a
        calculation.ov = b
        calculation.ow = c
        calculation.si = d
        calculation.sv = e 
        calculation.sw = f
        calculation.Transformer(calculation.values[0],calculation.values[1],calculation.values[2],calculation.values[3],calculation.values[4], calculation.values[5])
        Gui_values = calculation.print_calculation()


        self.label_Iw.setText(str(Gui_values[0]))
        self.label_Im.setText(str(Gui_values[1]))
        self.label_Ro.setText(str(Gui_values[2]))
        self.label_Xo.setText(str(Gui_values[3]))
        self.label_Ro1.setText(str(Gui_values[4]))
        self.label_Xo1.setText(str(Gui_values[5]))
        self.label_pf.setText(str(Gui_values[6]))

        self.background_img.setGeometry(0,0,790, 350)
        picture = QPixmap("circuit_diagram.jpg")
        self.background_img.setPixmap(picture)
        self.background_img.move(10, 20)

        self.diagram_Iw.setText(str(calculation.data.current_w()) + " A")
        self.diagram_Iw.move(97, 257)
        self.diagram_Iw.setFont(QtGui.QFont('Arial',9))

        self.diagram_Im.setText(str(calculation.data.current_m()) + " A")
        self.diagram_Im.move(415, 260)
        self.diagram_Im.setFont(QtGui.QFont('Arial',9))

        self.diagram_Xo.setText(str(calculation.data.impedence_o()) + " Ω")
        self.diagram_Xo.move(370, 182)
        self.diagram_Xo.setFont(QtGui.QFont('Arial',9))

        self.diagram_Ro.setText(str(calculation.data.resistance_o()) + " Ω")
        self.diagram_Ro.move(190, 182)
        self.diagram_Ro.setFont(QtGui.QFont('Arial',9))


        self.diagram_Ro1.setText(str(calculation.data.resistance_o1()) + " Ω")
        self.diagram_Ro1.move(450, 70)
        self.diagram_Ro1.setFont(QtGui.QFont('Arial',9))
        

        self.diagram_Xo1.setText(str(calculation.data.impedence_o1()) + " Ω")
        self.diagram_Xo1.move(600, 70)
        self.diagram_Xo1.setFont(QtGui.QFont('Arial',9))

    def clickme(self):
        self.linetext_oi.clear()
        self.linetext_ov.clear()
        self.linetext_ow.clear()
        self.linetext_si.clear()
        self.linetext_sv.clear()
        self.linetext_sw.clear()






def window():
    app = QApplication(sys.argv)
    win = Transformer_app()
    win.show()
    sys.exit(app.exec_())

window()
