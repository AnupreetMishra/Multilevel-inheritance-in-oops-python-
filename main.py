class Phone:
  def __init__(self):
      pass


  def dial(self,number):
      print("calling the number",number)


  def sms(self,number):
      print("sending SMS to",number)


class SmartPhone(Phone):
  def __init__(self):
      Phone.__init__(self)

  def internet(self):
      print("Surfing internet")


  def camera(self):
      print("camera is on")


class SmartPhoneLatestSeries(SmartPhone):
  def __init__(self):
      SmartPhone.__init__(self)


  def UpgradedAndroidVersion(self):
      print("UpgradedAndroidVersion is smooth")


  def facelock(self):
      print("secure the phone with faceklock")


samsung=Phone()
vivo=SmartPhone()
oneplus=SmartPhoneLatestSeries()


samsung.sms(8933026609)
vivo.sms(8933026609)
oneplus.sms(8933026609)
