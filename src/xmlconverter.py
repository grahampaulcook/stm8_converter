import xml.etree.ElementTree as ET

root = ET.parse("STM8S003F3.xml")

for module in root.findall(".//module"):
    modulename = module.attrib.get("name")

    for sfr in module.findall(".//SFR"):
        address = sfr.attrib.get("address")  # .replace("0x", "$")

        for d in sfr.findall(".//register"):
            description = d.attrib.get("description")
            name = d.attrib.get("name")

            print()
            print(";" + description)
            print(modulename + "_" + name + " EQU " + address)

            for bitfield in sfr.findall(".//bitfield"):
                bitfieldName = bitfield.attrib.get('name')
                bitfieldBits = bitfield.attrib.get('bits')

                bitfieldBitsSplit = bitfieldBits.split("-")

                if len(bitfieldBitsSplit) == 1:
                    print(bitfieldName + " EQU " + bitfieldBitsSplit[0])
                else:
                    # build the bitfield range
                    tmp = int(0)
                    for xx in range(int(bitfieldBitsSplit[0]), int(bitfieldBitsSplit[1]) + 1):
                        print(bitfieldName + str(tmp) + " EQU " + str(xx))
                        tmp += 1
