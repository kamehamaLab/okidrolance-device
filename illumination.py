import time
import board
import adafruit_bh1750

def main():
    # 初期化
    i2c = board.I2C()
    sensor = adafruit_bh1750.BH1750(i2c)

    # ルクスの表示
    while True:
        time.sleep(120)
        print("%.2f Lux"%sensor.lux)
    

if __name__ == "__main__":
    main()