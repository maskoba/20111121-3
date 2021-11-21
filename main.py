import os
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl
import pigpio

gpio_IN0 = 4    # GPIO4(7)
gpio_IN1 = 17   # GPIO17(11)
gpio_IN2 = 27   # GPIO27(13)
gpio_IN3 = 22   # GPIO22(15)
gpio_IN4 = 10   # GPIO10(19)
gpio_IN5 = 9    # GPIO9(21)

gpio_OUT0 = 14  # GPIO14(8)
gpio_OUT1 = 15  # GPIO15(10)
gpio_OUT2 = 23  # GPIO23(16)
gpio_OUT3 = 24  # GPIO24(18)

count = 0

def main():
    os.environ["QT_QUICK_CONTROLS_CONF"] = "./qtquickcontrols2.conf"

    app = QApplication([])
    engine = QQmlApplicationEngine()

    url = QUrl("./main.qml")
    # QML ファイルのロード
    engine.load(url)
    # ルートオブジェクトのリストが見つからない場合は
    # 起動できないため、終了する
    if not engine.rootObjects():
        sys.exit(-1)

    # 先頭の root オブジェクト (Main.qml 内の root オブジェクト ) を取得
    root = engine.rootObjects()[0]

    ret = app.exec_()

    pi.write(gpio_OUT0, 0)
    pi.write(gpio_OUT1, 0)
    pi.write(gpio_OUT2, 0)
    pi.write(gpio_OUT3, 0)

    sys.exit(ret)

# def counter_incr(self):
def counter_incr():
    global count
    if ( count == preset):
        return
    count += 1
    # self.lb3["text"] = '{:04}'.format(count)
    if ( count == preset):
        pi.write(gpio_OUT1, 1)


def interrupt(GPIO, level, tick):
    counter_incr()
    # app.counter_incr()

pi = pigpio.pi()   # GPIOにアクセスするためのインスタンスを作成
pi.set_mode(gpio_IN0, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN1, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN2, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN3, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN4, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_IN5, pigpio.INPUT)   # GPIO pin を入力設定
pi.set_mode(gpio_OUT0, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.set_mode(gpio_OUT1, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.set_mode(gpio_OUT2, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.set_mode(gpio_OUT3, pigpio.OUTPUT)   # GPIO pin を出力設定
pi.write(gpio_OUT0, 0)
pi.write(gpio_OUT1, 0)
pi.write(gpio_OUT2, 0)
pi.write(gpio_OUT3, 0)
pi.set_glitch_filter(gpio_IN0,10000)
pi.set_noise_filter(gpio_IN0, 1000, 500)
pi.callback(gpio_IN0, pigpio.FALLING_EDGE, interrupt)   # 割り込み処理用の関数

if __name__ == '__main__':
    main()