mult = 5
Horiz_Visible = 640 // mult
Horiz_FPorch = 16 // mult
Horiz_SPulse = 96 // mult
Horiz_BPorch = 48 // mult
Horiz_Total = Horiz_Visible + Horiz_FPorch + Horiz_SPulse + Horiz_BPorch

Vert_Visible = 480 // mult
Vert_FPorch = 10 // mult
Vert_SPulse = 2 // mult
Vert_BPorch = 33 // mult
Vert_Total = Vert_Visible + Vert_FPorch + Vert_SPulse + Vert_BPorch

def between(x: int, a: int, b: int) -> bool:
    return a <= x < b

with open("Horizontal_EEPROM.bin", "wb") as f:
    for i in range(Horiz_Total):
        outVal = 0xFF
        if(i < Horiz_Visible):
           outVal &= 0x00


        #This is the blanking interval of a VGA Signal
        if(i >= Horiz_Visible):
            outVal &= 0b11111110

        if(between(i, Horiz_Visible, Horiz_Visible + Horiz_FPorch)):
           outVal &= 0b11111101
           
        elif(between(i, Horiz_Visible + Horiz_FPorch, Horiz_Visible + Horiz_FPorch + Horiz_SPulse)):
            outVal &= 0b11111011
        elif(between(i, Horiz_Visible + Horiz_FPorch + Horiz_SPulse, Horiz_Visible + Horiz_FPorch + Horiz_SPulse + Horiz_BPorch)):
            outVal &= 0b11110111

        if i != Horiz_Total - 1:
            outVal |= 0b00010000

        f.write(outVal.to_bytes(1, byteorder="big"))
    for i in range(0x8000 - Horiz_Total):
        f.write(0b11101110.to_bytes(1, byteorder="big"))
        
        
        
with open("Vertical_EEPROM.bin", "wb") as f:
    for i in range(Vert_Total):
        outVal = 0xFF
        if(i < Vert_Visible):
           outVal &= 0x00
        #This is the blanking interval of a VGA Signal
        if(i >= Vert_Visible):
           outVal &= 0b11111110
        elif(between(i, Vert_Visible, Vert_Visible + Vert_FPorch)):
           outVal &= 0b11111101
        elif(between(i, Vert_Visible + Vert_FPorch, Vert_Visible + Vert_FPorch + Vert_SPulse)):
              outVal &= 0b11111011
        elif(between(i, Vert_Visible + Vert_FPorch + Vert_SPulse, Vert_Visible + Vert_FPorch + Vert_SPulse + Vert_BPorch)):
                outVal &= 0b11110111
                
        if i == Vert_Total - 1:
            outVal &= 0b11101111

        f.write(outVal.to_bytes(1, byteorder="big"))
    for i in range(0x8000 - Vert_Total):
        f.write(0b11101110.to_bytes(1, byteorder="big"))
