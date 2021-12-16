#! /APSshare/anaconda3/x86_64/bin/python

from pprint import pprint

from gestalt import *

styles = Stylesheet.parse("layout.yml")

a_display = Gestalt.Display(layout=styles["main_window"])

x_val = 4
y_val = 4

max_y = 385

for row in Spreadsheet.rows("faults.csv"):
	
	if row["Used"] == "X":
		a_display.addChild( Gestalt.Widget("caLed", layout=styles["status_led"]).
			position(x_val, y_val).
			setProperty("channel", "28ID:BLEPS:" + row["Name"]) )
		a_display.addChild( Gestalt.Widget("caLabel", layout=styles["fault_text"]).
			position(x_val + 25, y_val).
			setProperty("text", row["Name"]) )
	
		y_val += 20
	
		
	if y_val > max_y:
		y_val = 4
		x_val += 240
	
a_display.setProperty("geometry", Type.Rect(x_val + 240, max_y))
	
a_display.writeQt("faults.ui")
