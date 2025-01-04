with open('MachineCode.bin', 'wb') as f:
    # 0b1000000010010000
    f.write(b'\x80\x90')
    f.write(b'\x00\x02')
    f.write(b'\x85\x10')
    f.write(b'\x80\x07')