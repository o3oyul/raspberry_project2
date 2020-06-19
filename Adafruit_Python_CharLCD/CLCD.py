import time
import Adafruit_CharLCD as LCD
import socket
import sys

HOST = ''
PORT = 8866

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.message('Hello\nworld!')
time.sleep(2)
#lcd.clear()


try:
	s.bind((HOST, PORT))
except socket.error:
	print('Bind Failed')

print('Bind completed')
s.listen(10)
print('Socket awaiting messages')
conn, addr = s.accept()
print('Connected')

while True:
	data = conn.recv(1024)
	print(data)
	if data == 'quit':
		conn.sendall('quit')
		break

	#reply =  raw_input('yuripi : ')

	reply = 'good'
	if reply == 'quit':
		conn.sendall('quit')
		break
	conn.sendall(reply)

	lcd.clear()
	#showCLCD = data + '\n' + reply
	#lcd.message('temperature : ')
	lcd.message(data)
	#lcd.message('\nyuripi : ')
	#lcd.message(reply)

s.close()
conn.close()
