import xml.etree.ElementTree as ET

root = ET.parse("STM8AL3148.xml")

for elem in root.findall(".//module[@name='BEEP']//bitfield"):
    bitfieldName = elem.attrib.get('name')
    bitfieldBits = elem.attrib.get('bits')

    bitfieldBitsSplit = bitfieldBits.split("-")

    if len(bitfieldBitsSplit) == 1:
        print(bitfieldName + bitfieldBits)
    else:
        # build the bitfield range
        for xx in range(int(bitfieldBitsSplit[0]), int(bitfieldBitsSplit[1])):
            print( bitfieldName + str(xx) )
