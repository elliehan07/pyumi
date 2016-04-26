loadprofiles = LoadProfile(json,"OETotal",10)


lineweights = []
rawdata = js.loads(open(json).read())
usetypes = []
for n in rawdata.get("features"):
    feature = n.get("properties")
    usetype = feature.get("UseType")
    usetypes.append(usetype)
for i in usetypes:
    if i == "Residential and Lodging":
        lineweights.append(3.5)
    if i == "Office Spaces":
        lineweights.append(2)
    if i == "Retail":
        lineweights.append(1)
    if i == "Mixed use":
        lineweights.append(2.5)