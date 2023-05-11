# timeモジュールと補助モジュールをimport
import time
import smbus

def temp():
    i2c = smbus.SMBus(1)
    # i2cdetect で確認したアドレスを指定
    address = 0x5c
    
    # I2C初期化
    i2c.write_i2c_block_data(address, 0x00,[])
    i2c.write_i2c_block_data(address, 0x03,[0x00, 0x04])
    
    while True:
        time.sleep(120)
        # 温湿度情報読み出し
        block = i2c.read_i2c_block_data(address, 0, 6)
        
        # リトルエンディアン対応
        hum = block[2] << 8 | block[3]
        temp = block[4] << 8 | block[5]
        print(format(temp/10) + ' ℃')

def hum():
    i2c = smbus.SMBus(1)
    # i2cdetect で確認したアドレスを指定
    address = 0x5c
    
    # I2C初期化
    i2c.write_i2c_block_data(address, 0x00,[])
    i2c.write_i2c_block_data(address, 0x03,[0x00, 0x04])

    while True:
        time.sleep(120)
        # 温湿度情報読み出し
        block = i2c.read_i2c_block_data(address, 0, 6)
        
        # リトルエンディアン対応
        hum = block[2] << 8 | block[3]
        temp = block[4] << 8 | block[5]
        print(format( hum/10) + ' %')

if __name__ == "__main__":
    temp()
    hum()


